from fastapi import FastAPI
from routers import routers_v1

def create_app():
    app = FastAPI()
    app.include_router(routers_v1.router, prefix="/v1")
    return app
app = create_app()

