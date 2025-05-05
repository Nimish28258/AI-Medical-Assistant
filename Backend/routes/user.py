from fastapi import APIRouter, HTTPException
from models.user import User
from typing import List

router = APIRouter(prefix="/users", tags=["Users"])

users_db: List[User] = [] #Temporary in-mmemory database

@router.get('/', response_model = List[User])
def get_all_users():
    return users_db

@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@router.post("/", response_model=User)
def create_user(user: User):
    for u in users_db:
        if u.id == user.id:
            raise HTTPException(status_code=400, detail="User with this id already exists")
    users_db.append(user)
    return user

@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, updated_user: User):
    for index, user in enumerate(users_db):
        if user.id == user_id:
            users_db[index] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail = "User not found")

@router.delete("/{user_id}")
def delete_user(user_id: int):
    for index, user in enumerate(users_db):
        if user.id == user_id:
            users_db.pop(index)
            return {"message":"User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")