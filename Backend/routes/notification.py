from fastapi import APIRouter, HTTPException
from models.notification import Notification
from typing import List

router = APIRouter(prefix="/notifications", tags=["Notifications"])

# In-memory database
notifications_db: List[Notification] = []

@router.get("/", response_model=List[Notification])
def get_all_notifications():
    return notifications_db

@router.get("/{notification_id}", response_model=Notification)
def get_notification(notification_id: int):
    for notification in notifications_db:
        if notification.id == notification_id:
            return notification
    raise HTTPException(status_code=404, detail="Notification not found")

@router.post("/", response_model=Notification)
def create_notification(notification: Notification):
    for n in notifications_db:
        if n.id == notification.id:
            raise HTTPException(status_code=400, detail="Notification with this ID already exists")
    notifications_db.append(notification)
    return notification

@router.put("/{notification_id}", response_model=Notification)
def update_notification(notification_id: int, updated_notification: Notification):
    for index, notification in enumerate(notifications_db):
        if notification.id == notification_id:
            notifications_db[index] = updated_notification
            return updated_notification
    raise HTTPException(status_code=404, detail="Notification not found")

@router.delete("/{notification_id}")
def delete_notification(notification_id: int):
    for index, notification in enumerate(notifications_db):
        if notification.id == notification_id:
            notifications_db.pop(index)
            return {"message": "Notification deleted successfully"}
    raise HTTPException(status_code=404, detail="Notification not found")
