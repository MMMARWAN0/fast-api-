#app/crud.py

from typing import List, Dict, Optional
from .utils import read_users, write_users
from .models import User

def get_all_users() -> List[Dict]:
    return read_users()

def get_user_by_id(user_id: int) -> Optional[Dict]:
    users = read_users()
    return next((user for user in users if user["id"] == user_id), None)

def create_user(user_data: Dict) -> Dict:
    users = read_users()
    new_id = max([u["id"] for u in users], default=0) + 1
    new_user = {"id": new_id, **user_data}
    users.append(new_user)
    write_users(users)
    return new_user

def update_user(user_id: int, updates: Dict) -> Optional[Dict]:
    users = read_users()
    for user in users:
        if user["id"] == user_id:
            user.update({k: v for k, v in updates.items() if v is not None})
            write_users(users)
            return user
    return None

def delete_user(user_id: int) -> bool:
    users = read_users()
    new_users = [u for u in users if u["id"] != user_id]
    if len(new_users) == len(users):
        return False
    write_users(new_users)
    return True
