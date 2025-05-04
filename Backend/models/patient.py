from pydantic import BaseModel, EmailStr
from datetime import datetime

class Patient(BaseModel):
    id: int
    name: str
    age: int
    gender: str
    email: EmailStr
    phone: str
    address: str
    medical_record_number: str

    class Config:
        orm_mode = True
