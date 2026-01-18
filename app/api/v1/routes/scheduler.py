from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List, Optional
from fastapi import Query

from app.db.session import get_db
from app.models.generated_post import GeneratedPost
from app.models.scheduled_post import ScheduledPost
from app.schemas.scheduled_post import (
    ScheduledPostCreate,
    ScheduledPostResponse
)
allowed_platforms = {"facebook", "instagram","linkedin"}
router = APIRouter(prefix="/scheduler", tags=["scheduler"])

@router.post("/",response_model=ScheduledPostResponse, status_code=status.HTTP_201_CREATED)
def schedule_post(payload: ScheduledPostCreate,db: Session = Depends(get_db)):
    Generated_post = db.query(GeneratedPost).filter(payload.generated_post_id == GeneratedPost.id).first()

    if not Generated_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Generated post not found.")
    
    if payload.scheduled_at <= datetime.utcnow():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Scheduled time must be in the future.")
    
    if payload.platform.lower() not in allowed_platforms:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Unsupported platform.")
    
    scheduled_post = ScheduledPost(
        generated_post_id = payload.generated_post_id,
        platform = payload.platform.lower(),
        scheduled_at = payload.scheduled_at,
        status = "pending"
    )
    db.add(scheduled_post)
    db.commit()
    db.refresh(scheduled_post)

    return scheduled_post

@router.get("/queue", response_model=List[ScheduledPostResponse])
def get_scheduled_queue(status: Optional[str] = Query(default="pending"),limit: int = Query(default=20, le=100),db: Session = Depends(get_db)):
    query = db.query(ScheduledPost)
    if status:
        query = query.filter(ScheduledPost.status == status)
    scheduled_posts = query.order_by(ScheduledPost.scheduled_at.asc()).limit(limit).all()
    return scheduled_posts

