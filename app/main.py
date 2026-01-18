from fastapi import FastAPI
from app.api.v1.routes.generator import router as generator_router
from app.db.session import engine
from app.db.base import Base
from app.models import generated_post
from app.api.v1.routes.scheduler import router as scheduler_router

def create_app():
    app = FastAPI(
        title="Soft.json Publish Backend",
        version="1.0.0"
    )

    Base.metadata.create_all(bind=engine)

    app.include_router(generator_router, prefix="/api/v1/generator")
    app.include_router(scheduler_router, prefix="/api/v1")
    return app

app = create_app()