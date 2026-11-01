# QuestForge

A tiny text-adventure engine you run in the terminal. The story lives in a
JSON world file - move between rooms and look around. Your squad grows the
world one ticket at a time.

## Run it

```bash
python main.py
```

## Run the tests

```bash
python -m unittest
```

## How it's laid out

| File | What it does |
|---|---|
| `main.py` | The menu loop you interact with |
| `storage.py` | Loads and saves the JSON data file |
| `features/core.py` | The world, moving between rooms, and small helpers |
| `features/reports.py` | Summary reports (half-built - finish it via a ticket) |
| `data/questforge.json` | The room graph and move history |
| `tests/test_core.py` | Example tests to copy from |
| `tests/test_neighbors.py` | Tests for `neighbors(data, room_key)` in `features/core.py` |

## Helpers

- `neighbors(data, room_key)` in `features/core.py`: returns the list of room keys reachable directly from a room (empty list for a dead end).

## Team

<!-- Add yourself here on your Git lesson: - Your Name (role) -->

- Michael

## Where to start

Pick a ticket from the `tickets/` folder (or the Issues tab once your section
repo exists). Read `CONTRIBUTING.md` for the Definition of Done every pull
request has to meet.
