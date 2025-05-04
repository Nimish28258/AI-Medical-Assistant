from pydantic import BaseModel
from typing import Optional

class AIResponse(BaseModel):
    id: int
    query_id: int  # ForeignKey reference to PatientQuery
    response_text: str
    confidence_score: Optional[float] = None  # Optional field for confidence

    class Config:
        orm_mode = True
