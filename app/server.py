from fastapi import FastAPI
from app.api.V1.controllers import routerQuestions
from fastapi.middleware.cors import CORSMiddleware

def init_routers(app_: FastAPI) -> None:
    app_.include_router(routerQuestions)


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="Estuda AI - API",
        description="FastAPI Estuda AI - API",
        version="1.0.0",
    )

    app_.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],  
        allow_headers=["*"],
    )
    init_routers(app_=app_)
    return app_

app = create_app()
