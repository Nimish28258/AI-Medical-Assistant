from pydantic import BaseModel
from datetime import datetime

class PatientQuery(BaseModel):
    id: int
    patient_id: int  # ForeignKey reference
    query_text: str
    timestamp: datetime

    class Config:
        orm_mode = True
