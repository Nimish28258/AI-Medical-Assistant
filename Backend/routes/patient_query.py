from fastapi import APIRouter, HTTPException
from models.patient_query import PatientQuery
from typing import List

router = APIRouter(prefix="/patient-queries", tags=["Patient Queries"])

# In-memory "database"
queries_db: List[PatientQuery] = []

@router.get("/", response_model=List[PatientQuery])
def get_all_queries():
    return queries_db

@router.get("/{query_id}", response_model=PatientQuery)
def get_query(query_id: int):
    for query in queries_db:
        if query.id == query_id:
            return query
    raise HTTPException(status_code=404, detail="Query not found")

@router.post("/", response_model=PatientQuery)
def create_query(query: PatientQuery):
    for q in queries_db:
        if q.id == query.id:
            raise HTTPException(status_code=400, detail="Query with this ID already exists")
    queries_db.append(query)
    return query

@router.put("/{query_id}", response_model=PatientQuery)
def update_query(query_id: int, updated_query: PatientQuery):
    for index, query in enumerate(queries_db):
        if query.id == query_id:
            queries_db[index] = updated_query
            return updated_query
    raise HTTPException(status_code=404, detail="Query not found")

@router.delete("/{query_id}")
def delete_query(query_id: int):
    for index, query in enumerate(queries_db):
        if query.id == query_id:
            queries_db.pop(index)
            return {"message": "Query deleted successfully"}
    raise HTTPException(status_code=404, detail="Query not found")
