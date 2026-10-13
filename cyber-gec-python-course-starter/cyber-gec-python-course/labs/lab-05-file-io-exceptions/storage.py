"""Lab 05 starter: JSON persistence and safe error handling."""
from pathlib import Path
DATA_FILE = Path("project/data/members.json")

def save_members(members):
    # TODO: Create parent directory and safely write JSON.
    # Consider a temporary file and backup strategy.
    pass

def load_members():
    # TODO: Load JSON, validate structure, handle expected exceptions.
    # Never silently replace corrupted data with an empty database.
    pass
