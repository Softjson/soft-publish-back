from fastapi import APIRouter
from app.schemas.post import PostGenerateRequest, PostGenerateResponse
from app.services.ai import generate_post

router = APIRouter()

@router.get("/ping")
def ping():
    return {"message": "Generator service OK"}

@router.post("/", response_model=PostGenerateResponse)
def create_generated_post(data: PostGenerateRequest):
    """
    Endpoint principal para generar publicaciones automáticas usando IA.
    """
    result = generate_post(topic=data.topic, style=data.style)
    return PostGenerateResponse(content=result)
