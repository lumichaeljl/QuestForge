import unittest
from features import reports


class TestAverageRooms(unittest.TestCase):
    def test_average_of_several_values(self):
        self.assertEqual(reports.average_rooms({"history": [5, 6, 4]}), 5.0)

    def test_empty_history_returns_zero(self):
        self.assertEqual(reports.average_rooms({"history": []}), 0.0)


if __name__ == "__main__":
    unittest.main()