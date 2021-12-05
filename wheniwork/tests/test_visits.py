import unittest

from wheniwork.util.visits import add_visit, PathVisit


class TestVisits(unittest.TestCase):

    def test_unseen_path(self):
        data = {}
        visit = PathVisit('1', '/path', 10)

        add_visit(data, visit)

        self.assertEqual(data, {visit.user_id: {visit.path: visit.length}})  # add assertion here

    def test_seen_path(self):
        visit = PathVisit('1', '/path', 10)
        data = {visit.user_id: {visit.path: visit.length}}
        add_visit(data, visit)

        self.assertEqual(data, {visit.user_id: {visit.path: visit.length*2}})


if __name__ == '__main__':
    unittest.main()
