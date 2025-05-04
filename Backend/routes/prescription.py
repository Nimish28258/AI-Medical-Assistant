from fastapi import APIRouter
from models.prescription import Prescription

router = APIRouter(prefix="/prescriptions", tags=["Prescriptions"])

@router.get("/")
def get_all_prescriptions():
    pass

@router.get("/{prescription_id}")
def get_prescription(prescription_id: int):
    pass

@router.post("/")
def create_prescription(prescription: Prescription):
    pass

@router.put("/{prescription_id}")
def update_prescription(prescription_id: int, prescription: Prescription):
    pass

@router.delete("/{prescription_id}")
def delete_prescription(prescription_id: int):
    pass
