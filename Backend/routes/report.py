from fastapi import APIRouter
from models.report import Report

router = APIRouter(prefix="/reports",tags=["Reports"])

@router.get("")
def get_all_reports():
    pass

@router.get("/{report_id}")
def get_report(report_id: int):
    pass

@router.post("/")
def create_report(report: Report):
    pass

@router.put("/{report_id}")
def update_report(report_id: int , report: Report):
    pass

@router.delete("/{report_id}")
def delete_report(report_id: int):
    pass