from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MedicalHistory(BaseModel):
    id: int
    patient_id: int
    condition: str
    notes: Optional[str] = None
    recorded_on: datetime

    class Config:
        orm_mode = True
    