import unittest
from unittest.mock import MagicMock, patch, mock_open

import webtraffictransformation.util.file_utils
from webtraffictransformation.util.file_utils import read_file, write_file
from webtraffictransformation.util.visits import Visit, CombinedVisits


class TestReadFile(unittest.TestCase):
    # Stub the file download
    webtraffictransformation.util.file_utils.urlopen = lambda x: MagicMock()
    header = ['a', 'b', 'c', 'd', 'e']

    def test_read_empty_file(self):
        webtraffictransformation.util.file_utils.reader = lambda x: [self.header]

        result = read_file('url')
        self.assertEqual(result, [])

    def test_read_file_one_row(self):
        row = ['1', '7', '/', 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0	',
               '378']
        webtraffictransformation.util.file_utils.reader = lambda x: [self.header, row]

        result = read_file('url')
        self.assertEqual(result, [Visit('378', '/', 7)])

    def test_read_file_two_rows_same_user(self):
        row1 = ['1', '7', '/', 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0	',
                '378']
        row2 = ['1', '7', '/', 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0	',
                '378']
        webtraffictransformation.util.file_utils.reader = lambda x: [self.header, row1, row2]

        result = read_file('url')
        self.assertEqual(result, [Visit('378', '/', 7), Visit('378', '/', 7)])

    def test_read_file_two_rows_different_user(self):
        row1 = ['1', '7', '/', 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0	',
                '378']
        row2 = ['1', '7', '/', 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0	',
                '100']
        webtraffictransformation.util.file_utils.reader = lambda x: [self.header, row1, row2]

        result = read_file('url')
        self.assertEqual(result, [Visit('378', '/', 7), Visit('100', '/', 7)])


class TestWriteFile(unittest.TestCase):
    mockCsv = []

    def setUp(self):
        self.mockCsv = []

    @patch('builtins.open', new_callable=mock_open())
    def test_write_no_data(self, mock_open_file):
        write_file([], CombinedVisits(), 'path')
        mock_open_file.return_value.__enter__().write.assert_called_once_with('user_id\r\n')

    @patch('builtins.open', new_callable=mock_open())
    def test_write_one_user(self, mock_open_file):
        paths = ['/test1', '/test2']
        visits = CombinedVisits()
        visits.data = {'1': {'/test1': 100, '/test2': 200}}

        write_file(paths, visits, 'path')
        mock_open_file.return_value.__enter__().write.assert_called_with('1,100,200\r\n')


if __name__ == '__main__':
    unittest.main()
