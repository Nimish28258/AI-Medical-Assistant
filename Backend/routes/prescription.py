from fastapi import APIRouter, HTTPException
from models.prescription import Prescription
from typing import List

router = APIRouter(prefix="/prescriptions", tags=["Prescriptions"])

prescription_db: List[Prescription] = []

@router.get("/", response_model=List[Prescription])
def get_all_prescriptions():
    return prescription_db

@router.get("/{prescription_id}", response_model = Prescription)
def get_prescription(prescription_id: int):
    for prescription in prescription_db:
        if prescription.id == prescription_id:
            return prescription
    raise HTTPException(status_code=404, detail="Prescription not found")

@router.post("/", response_model=Prescription)
def create_prescription(prescription: Prescription):
    for p in prescription_db:
        if p.id == prescription.id:
            raise HTTPException(status_code=400, detail="Prescription with this id already exists")
    prescription_db.append(prescription)
    return prescription

@router.put("/{prescription_id}", response_model=Prescription)
def update_prescription(prescription_id: int, updated_prescription: Prescription):
    for index, prescription in enumerate(prescription_db):
        if prescription.id == prescription_id:
            prescription[index] = updated_prescription
            return updated_prescription
    raise HTTPException(status_code=404, detail="Prescription not found")

@router.delete("/{prescription_id}")
def delete_prescription(prescription_id: int):
    for index, prescription in enumerate(prescription_db):
        if prescription.id == prescription_id:
            prescription_db.pop(index)
            return{"messsage":"Prescription deleted successfully"}
    raise HTTPException(status_code=404, detail="Prescription not found")