from pydantic import BaseModel
from datetime import datetime
from typing import List

class Prescription(BaseModel):
    id: int
    patient_id: int
    doctor_name: str
    medications: List[str]  # Can also use a more complex structure if needed
    prescribed_on: datetime

    class Config:
        orm_mode = True
