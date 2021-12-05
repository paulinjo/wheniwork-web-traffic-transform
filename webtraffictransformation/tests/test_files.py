import unittest
from unittest.mock import MagicMock, patch, mock_open

import webtraffictransformation.util.files
from webtraffictransformation.util.files import read_file
from webtraffictransformation.util.visits import PathVisit


class TestReadFile(unittest.TestCase):
    # Stub the file download
    webtraffictransformation.util.files.urlopen = lambda x: MagicMock()
    header = ['a', 'b', 'c', 'd', 'e']

    def test_read_empty_file(self):
        webtraffictransformation.util.files.reader = lambda x: [self.header]

        result = read_file('url')
        self.assertEqual(result, [])

    def test_read_file_one_row(self):
        row = ['1', '7', '/', 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0	',
               '378']
        webtraffictransformation.util.files.reader = lambda x: [self.header, row]

        result = read_file('url')
        self.assertEqual(result, [PathVisit('378', '/', 7)])

    def test_read_file_two_rows_same_user(self):
        row1 = ['1', '7', '/', 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0	',
                '378']
        row2 = ['1', '7', '/', 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0	',
                '378']
        webtraffictransformation.util.files.reader = lambda x: [self.header, row1, row2]

        result = read_file('url')
        self.assertEqual(result, [PathVisit('378', '/', 7), PathVisit('378', '/', 7)])

    def test_read_file_two_rows_different_user(self):
        row1 = ['1', '7', '/', 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0	',
                '378']
        row2 = ['1', '7', '/', 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0	',
                '100']
        webtraffictransformation.util.files.reader = lambda x: [self.header, row1, row2]

        result = read_file('url')
        self.assertEqual(result, [PathVisit('378', '/', 7), PathVisit('100', '/', 7)])


class TestWriteFile(unittest.TestCase):
    mockCsv = []

    # webtraffictransformation.util.files. = lambda x: MagicMock()

    def setUp(self):
        self.mockCsv = []

    @patch('builtins.open', new_callable=mock_open())
    def test_write_no_data(self, mock_open_file):
        webtraffictransformation.util.files.write_file([], {}, 'path')
        mock_open_file.return_value.__enter__().write.assert_called_once_with('user_id\r\n')

    @patch('builtins.open', new_callable=mock_open())
    def test_write_one_user(self, mock_open_file):
        paths = ['/test1', '/test2']
        visits = {'1': {'/test1': 100, '/test2': 200}}

        webtraffictransformation.util.files.write_file(paths, visits, 'path')
        mock_open_file.return_value.__enter__().write.assert_called_with('1,100,200\r\n')


if __name__ == '__main__':
    unittest.main()
