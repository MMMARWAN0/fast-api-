#app/utils.py

import json
import os
from typing import List, Dict

DATA_FILE = "data/users.json"

# Ensure file exists
if not os.path.exists(DATA_FILE):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

def read_users() -> List[Dict]:
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def write_users(users: List[Dict]) -> None:
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)
