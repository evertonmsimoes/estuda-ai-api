from fastapi import FastAPI
from app.api.V1.controllers import routerQuestions

def init_routers(app_: FastAPI) -> None:
    app_.include_router(routerQuestions)


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="Estuda AI - API",
        description="FastAPI Estuda AI - API",
        version="1.0.0",
    )
    init_routers(app_=app_)
    return app_

app = create_app()
