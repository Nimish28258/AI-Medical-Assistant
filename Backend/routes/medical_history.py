from fastapi import APIRouter
from models.medical_history import MedicalHistory

router = APIRouter(prefix="/medical-history", tags=["Medical History"])

@router.get("/")
def get_all_medical_history():
    pass

@router.get("/{history_id}")
def get_medical_history(history_id: int):
    pass

@router.post("/")
def create_medical_history(history: MedicalHistory):
    pass

@router.put("/{history_id}")
def update_medical_history(history_id: int, history: MedicalHistory):
    pass

@router.delete("/{history_id}")
def delete_medical_history(history_id: int):
    pass
