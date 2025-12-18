from pydantic import BaseModel, Field
from datetime import datetime

class PostGenerateRequest(BaseModel):
    topic: str = Field(..., min_length=3, max_length=100)
    style: str = Field(default="profesional", max_length=50)
    template: str = "instagram_post"

class PostGenerateResponse(BaseModel):
    content: str

class GeneratedPostOut(BaseModel):
    id: int
    topic: str
    style: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True