from fastapi import APIRouter
from models.ai_response import AIResponse

router = APIRouter(prefix="/ai-responses", tags=["AI Responses"])

@router.get("/")
def get_all_ai_responses():
    pass

@router.get("/{response_id}")
def get_ai_response(response_id: int):
    pass

@router.post("/")
def create_ai_response(response: AIResponse):
    pass

@router.put("/{response_id}")
def update_ai_response(response_id: int, response: AIResponse):
    pass

@router.delete("/{response_id}")
def delete_ai_response(response_id: int):
    pass