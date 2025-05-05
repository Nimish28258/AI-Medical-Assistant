from fastapi import APIRouter, HTTPException
from models.appointment import Appointment
from typing import List

router = APIRouter(prefix="/appointments", tags=["Appointments"])

# In-memory list to store appointment records
appointments_db: List[Appointment] = []

@router.get("/", response_model=List[Appointment])
def get_all_appointments():
    return appointments_db

@router.get("/{appointment_id}", response_model=Appointment)
def get_appointment(appointment_id: int):
    for appt in appointments_db:
        if appt.id == appointment_id:
            return appt
    raise HTTPException(status_code=404, detail="Appointment not found")

@router.post("/", response_model=Appointment)
def create_appointment(appointment: Appointment):
    for appt in appointments_db:
        if appt.id == appointment.id:
            raise HTTPException(status_code=400, detail="Appointment with this ID already exists")
    appointments_db.append(appointment)
    return appointment

@router.put("/{appointment_id}", response_model=Appointment)
def update_appointment(appointment_id: int, appointment: Appointment):
    for index, appt in enumerate(appointments_db):
        if appt.id == appointment_id:
            appointments_db[index] = appointment
            return appointment
    raise HTTPException(status_code=404, detail="Appointment not found")

@router.delete("/{appointment_id}")
def delete_appointment(appointment_id: int):
    for index, appt in enumerate(appointments_db):
        if appt.id == appointment_id:
            appointments_db.pop(index)
            return {"message": "Appointment deleted successfully"}
    raise HTTPException(status_code=404, detail="Appointment not found")
