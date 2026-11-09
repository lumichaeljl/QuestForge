import tempfile
import unittest
from pathlib import Path

import storage


class TestSaveLoad(unittest.TestCase):
    def test_saved_room_loads_back(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "save.json"
            data = {"start": "entrance", "rooms": {}, "saved_room": "library"}
            storage.save_data(data, path)
            self.assertEqual(storage.load_data(path)["saved_room"], "library")


if __name__ == "__main__":
    unittest.main()