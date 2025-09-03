#app/main.py

from fastapi import FastAPI, HTTPException
from typing import List
from app.schemas import UserCreate, UserUpdate
from app.models import User
import app.crud as crud


app = FastAPI(title="User API with JSON Storage")

@app.get("/users", response_model=List[User])
def get_users():
    return crud.get_all_users()

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    user = crud.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users", response_model=User, status_code=201)
def create_user(user: UserCreate):
    return crud.create_user(user.dict())

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user_update: UserUpdate):
    updated_user = crud.update_user(user_id, user_update.dict())
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int):
    success = crud.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return
