from pydantic import BaseModel, EmailStr
from datetime import datetime

class User(BaseModel):
    id: int
    username: str
    email: EmailStr
    password_hash: str
    role: str
    created_at: datetime

    class Config: 
        orm_mode = True