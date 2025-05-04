from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Appointment(BaseModel):
    id: int
    patient_id: int
    doctor_name: str
    appointment_time: datetime
    status: str  # pending, confirmed, completed

    class Config:
        orm_mode = True
