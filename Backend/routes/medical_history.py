from fastapi import APIRouter, HTTPException
from models.medical_history import MedicalHistory
from typing import List

router = APIRouter(prefix="/medical-history", tags=["Medical History"])

# In-memory list to store medical history records
medical_history_db: List[MedicalHistory] = []

@router.get("/", response_model=List[MedicalHistory])
def get_all_medical_history():
    return medical_history_db

@router.get("/{history_id}", response_model=MedicalHistory)
def get_medical_history(history_id: int):
    for record in medical_history_db:
        if record.id == history_id:
            return record
    raise HTTPException(status_code=404, detail="Medical history not found")

@router.post("/", response_model=MedicalHistory)
def create_medical_history(history: MedicalHistory):
    for record in medical_history_db:
        if record.id == history.id:
            raise HTTPException(status_code=400, detail="Medical history with this ID already exists")
    medical_history_db.append(history)
    return history

@router.put("/{history_id}", response_model=MedicalHistory)
def update_medical_history(history_id: int, history: MedicalHistory):
    for index, record in enumerate(medical_history_db):
        if record.id == history_id:
            medical_history_db[index] = history
            return history
    raise HTTPException(status_code=404, detail="Medical history not found")

@router.delete("/{history_id}")
def delete_medical_history(history_id: int):
    for index, record in enumerate(medical_history_db):
        if record.id == history_id:
            medical_history_db.pop(index)
            return {"message": "Medical history deleted successfully"}
    raise HTTPException(status_code=404, detail="Medical history not found")
