from fastapi import FastAPI
from app.api.v1.routes.generator import router as generator_router

def create_app():
    app = FastAPI(
        title="Soft.json Publish Backend",
        version="1.0.0"
    )

    app.include_router(generator_router, prefix="/api/v1/generator")

    return app

app = create_app()