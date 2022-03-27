from fastapi import FastAPI
from uvicorn import run

from src.utils.db_manager import init_db
from src.utils.log_manager import init_logging
from src.utils.env_constants import HOSTNAME, PORT, RELOAD, LOGLEVEL
from src.routes.v1.root_router import root_router
from src.routes.v1.car_router import car_router
from src.routes.v1.user_router import user_router


app = FastAPI(
    title="Sandbox FastApi Service",
    description="This is a sandbox for showcasing configs or methodologies",
    docs_url="/",
    version="pre-release",
    openapi_url="/api/v1/openapi.json",
)

init_logging()


@app.on_event("startup")
async def startup_events() -> None:
    """
    Startup tasks
    init_db() -> establishes db connection
    """
    init_db(app)


app.include_router(root_router)


if __name__ == "__main__":
    run("src.main:app", host=HOSTNAME, port=int(PORT), reload=RELOAD, log_level=LOGLEVEL)
