"""Tests for the neighbors helper."""

import unittest

from features import core


class TestNeighbors(unittest.TestCase):
    def setUp(self):
        self.data = {
            "start": "hall",
            "rooms": {
                "hall": {"description": "A hall.", "exits": {"north": "library", "east": "kitchen"}},
                "library": {"description": "A library.", "exits": {"south": "hall"}},
                "kitchen": {"description": "A kitchen.", "exits": {}},
            },
        }

    def test_room_with_multiple_exits(self):
        self.assertEqual(core.neighbors(self.data, "hall"), ["library", "kitchen"])

    def test_dead_end_returns_empty_list(self):
        self.assertEqual(core.neighbors(self.data, "kitchen"), [])


if __name__ == "__main__":
    unittest.main()