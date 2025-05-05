from fastapi import APIRouter, HTTPException
from models.report import Report
from typing import List

router = APIRouter(prefix="/reports",tags=["Reports"])

reports_db: List[Report] = []

@router.get("/", response_model=List[Report])
def get_all_reports():
    return reports_db

@router.get("/{report_id}", response_model=Report)
def get_report(report_id: int):
    for report in reports_db:
        if report.id == report_id:
            return report
    raise HTTPException(status_code=404, detail="Report not found")

@router.post("/", response_model=Report)
def create_report(report: Report):
    for r in reports_db:
        if r.id == report.id:
            raise HTTPException(status_code=400, detail="Report eith this ID already exists")
    reports_db.append(report)
    return report

@router.put("/{report_id}", response_model=Report)
def update_report(report_id: int , updated_report: Report):
    for index, report in enumerate(reports_db):
        if report.id == report_id:
            reports_db[index] = updated_report
            return updated_report
    raise HTTPException(status_code=404, detail="Report not found")

@router.delete("/{report_id}")
def delete_report(report_id: int):
    for index, report in enumerate(reports_db):
        if report.id == report_id:
            reports_db.pop(index)
            return{"Message":"Report deleted successfully"}
    raise HTTPException(status_code=404, detail="Report not found")