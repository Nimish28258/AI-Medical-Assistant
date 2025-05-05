from fastapi import APIRouter, HTTPException
from models.patient import Patient
from typing import List

router = APIRouter(prefix="/patients", tags=["Patients"])

patients_db: List[Patient] = []

@router.get("/", response_model=List[Patient])
def get_all_patients():
    return patients_db

@router.get("/{patient_id}", response_model = Patient)
def get_patient(patient_id: int):
    for patient in patients_db:
        if patient.id == patient_id:
            return patient
    raise HTTPException(status_code=404, detail="Patient not found")

@router.post("/", response_model = Patient)
def create_patient(patient: Patient):
    for patient in patients_db:
        if patient.id == patient.id:
            raise HTTPException(status_code=400, detail="Patient with this ID already exists")
    patients_db.append(patient)
    return patient

@router.put("/{patient_id}", response_model = Patient)
def update_patient(patient_id: int, updated_patient: Patient):
    for index , patient in enumerate(patients_db):
        if patient.id == patient_id:
            patients_db[index] = updated_patient
            return updated_patient
    raise HTTPException(status_code=404, detail="Patient not found")

@router.delete("/{patient_id}")
def delete_patient(patient_id: int):
    for index, patient in enumerate(patients_db):
        if patient.id == patient_id:
            patients_db.pop(index)
            return {"message":"Patient deleted Successfully"}
    raise HTTPException(status_code=404, detail="Patient not found")