from fastapi import APIRouter
from models.user import User

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
def get_all_users():
    pass

@router.get("/{user_id}")
def get_user(user_id: int):
    pass

@router.post("/")
def create_user(user: User):
    pass

@router.put("/{user_id}")
def update_user(user_id: int, user: User):
    pass

@router.delete("/{user_id}")
def delete_user(user_id:int):
    pass
