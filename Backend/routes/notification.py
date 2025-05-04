from fastapi import APIRouter
from models.notification import Notification

router = APIRouter(prefix="/notifications", tags=["Notifications"])

@router.get("/")
def get_all_notifications():
    pass

@router.get("/{notification_id}")
def get_notification(notification_id: int):
    pass

@router.post("/")
def create_notification(notification: Notification):
    pass

@router.put("/{notification_id}")
def update_notification(notification_id: int, notification: Notification):
    pass

@router.delete("/{notification_id}")
def delete_notification(notification_id: int):
    pass
