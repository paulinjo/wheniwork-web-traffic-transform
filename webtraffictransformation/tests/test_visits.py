import unittest

from webtraffictransformation.util.visits import CombinedVisits, Visit


class TestVisits(unittest.TestCase):

    def test_unseen_path(self):
        visits = CombinedVisits()
        visit = Visit('1', '/path', 10)

        visits.add(visit)

        self.assertEqual(visits.data, {visit.user_id: {visit.path: visit.length}})

    def test_seen_path(self):
        visit = Visit('1', '/path', 10)
        visits = CombinedVisits()
        visits.data = {visit.user_id: {visit.path: visit.length}}
        visits.add(visit)

        self.assertEqual(visits.data, {visit.user_id: {visit.path: visit.length * 2}})


if __name__ == '__main__':
    unittest.main()
