from datetime import datetime
from pydantic import BaseModel, Field

class ScheduledPostCreate(BaseModel):
    generated_post_id: int 
    platform: str = Field(..., example= "Instagram")
    scheduled_at: datetime = Field(..., example="2026-01-20T15:00:00")

class ScheduledPostResponse(BaseModel):
    id: int
    generated_post_id: int
    platform: str
    scheduled_at: datetime
    status: str
    created_at: datetime

    class Config:
        from_attributes = True