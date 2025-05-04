from fastapi import APIRouter
from models.appointment import Appointment

router = APIRouter(prefix="/appointments", tags=["Appointments"])

@router.get("/")
def get_all_appointments():
    pass

@router.get("/{appointment_id}")
def get_appointment(appointment_id: int):
    pass

@router.post("/")
def create_appointment(appointment: Appointment):
    pass

@router.put("/{appointment_id}")
def update_appointment(appointment_id: int, appointment: Appointment):
    pass

@router.delete("/{appointment_id}")
def delete_appointment(appointment_id: int):
    pass
