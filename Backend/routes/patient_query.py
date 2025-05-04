from fastapi import APIRouter
from models.patient_query import PatientQuery

router = APIRouter(prefix="/patient-queries", tags=["Patient Queries"])

@router.get("/")
def get_all_queries():
    pass

@router.get("/{query_id}")
def get_query(query_id: int):
    pass

@router.post("/")
def create_query(query: PatientQuery):
    pass

@router.put("/{query_id}")
def update_query(query_id: int, query: PatientQuery):
    pass

@router.delete("/{query_id}")
def delete_query(query_id: int):
    pass
