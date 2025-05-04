from fastapi import FastAPI
import uvicorn

from routes.ai_response import router as ai_response_router
from routes.appointment import router as appointment_router
from routes.medical_history import router as medical_history_router
from routes.notification import router as notification_router
from routes.patient_query import router as patient_query_router
from routes.patient import router as patient_router
from routes.prescription import router as prescription_router
from routes.report import router as report_router
from routes.user import router as user_router

app = FastAPI(
    title="AI-Medical-Assistant",
    description="APIs for managing patient data, appointments, queries, and AI responses."
)

app.include_router(ai_response_router)
app.include_router(appointment_router)
app.include_router(medical_history_router)
app.include_router(notification_router)
app.include_router(patient_query_router)
app.include_router(patient_router)
app.include_router(prescription_router)
app.include_router(report_router)
app.include_router(user_router)

if __name__ == "__main__":
    uvicorn("app:app", host="0.0.0.0", port=8000, reload=True)