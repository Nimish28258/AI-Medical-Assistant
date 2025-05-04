from pydantic import BaseModel
from datetime import datetime

class Report(BaseModel):
    id: int
    patient_id: int  # ForeignKey reference
    report_type: str  # e.g., lab result, AI summary
    content: str
    generated_on: datetime

    class Config:
        orm_mode = True
