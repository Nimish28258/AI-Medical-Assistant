from fastapi import APIRouter
from models.patient import Patient

router = APIRouter(prefix="/patients", tags=["Patients"])

@router.get("/")
def get_all_patients():
    pass

@router.get("/{patient_id}")
def get_patient(patient_id: int):
    pass

@router.post("/")
def create_patient(patient: Patient):
    pass

@router.put("/{patient_id}")
def update_patient(patient_id: int, patient: Patient):
    pass

@router.delete("/{patient_id}")
def delete_patient(patient_id: int):
    pass
