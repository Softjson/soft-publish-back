from fastapi import FastAPI

def create_app():
    app = FastAPI(
        title="Soft.json Publish Backend",
        description="Backend service for publishing Soft.json files.",
        version="1.0.0"
    )
    return app

app = create_app()