from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.post import PostGenerateRequest, PostGenerateResponse, GeneratedPostOut
from app.db.session import get_db
from app.models.generated_post import GeneratedPost
from app.services.ai import generate_post
from app.services.templates_service import (
    build_prompt
)

router = APIRouter()

@router.get("/ping")
def ping():
    return {"message": "Generator service OK"}

@router.post("/", response_model=PostGenerateResponse)
def create_generated_post(data: PostGenerateRequest,db: Session = Depends(get_db)):
    """
    Endpoint principal para generar publicaciones automáticas usando IA.
    """

    prompt = build_prompt(
        template_key=data.template,
        topic=data.topic,
        style=data.style
    )

    result = generate_post(prompt=prompt)
    
    post = GeneratedPost(
        topic=data.topic,
        style=data.style,
        content=result,
        template_key=data.template
    )

    db.add(post)
    db.commit()
    db.refresh(post)

    return PostGenerateResponse(content=result)


@router.get("/history", response_model=list[GeneratedPostOut])
def get_generated_posts(
    db: Session = Depends(get_db),
    limit: int = 20
):
    """
    Retorna el historial de publicaciones generadas.
    """
    posts = (
        db.query(GeneratedPost)
        .order_by(GeneratedPost.created_at.desc())
        .limit(limit)
        .all()
    )
    return posts
