from pydantic import BaseModel
from datetime import datetime

class PostGenerateRequest(BaseModel):
    topic: str
    style: str = "Profesional y creativo"

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