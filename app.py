from fastapi import FastAPI
from routers import routers_v1
from routers import routers_health

def create_app():
    app = FastAPI()
    # v1 api
    app.include_router(routers_v1.router, prefix="/v1")
    # health check
    app.include_router(routers_health.router)
    return app
app = create_app()

