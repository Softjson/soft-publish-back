from pydantic import BaseModel

class PostGenerateRequest(BaseModel):
    topic: str
    style: str = "Profesional y creativo"

class PostGenerateResponse(BaseModel):
    content: str
