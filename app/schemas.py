#app/schemas.py

from typing import Optional
from pydantic import BaseModel, EmailStr

# Schema for creating a new user
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: Optional[int] = None

# Schema for updating an existing user
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = None
