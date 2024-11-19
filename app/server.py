from fastapi import FastAPI

def init_routers(app_: FastAPI) -> None:
    pass


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="Estuda AI - API",
        description="FastAPI Estuda AI - API",
        version="1.0.0",
    )
    init_routers(app_=app_)
    return app_

app = create_app()
