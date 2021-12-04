import unittest
from wheniwork.app import *


class TestApp(unittest.TestCase):

    def test_append_new_path(self):
        data = {}
        user = '1'
        path = '/path'
        length = 10
        add_visit(data, user, path, length)

        self.assertEqual(data, {user: {path: length}})  # add assertion here


    def test_append_existing_path(self):
        user = '1'
        path = '/path'
        length = 10
        data = {user: {path: length}}
        add_visit(data, user, path, length)

        self.assertEqual(data, {user: {path: length*2}})

if __name__ == '__main__':
    unittest.main()
