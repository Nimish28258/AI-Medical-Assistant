from pydantic import BaseModel
from datetime import datetime

class Notification(BaseModel):
    id: int
    patient_id: int
    title: str
    message: str
    created_at: datetime
    read: bool

    class Config:
        orm_mode = True
