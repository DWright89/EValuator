from fastapi import FastAPI
from uvicorn import run
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from src.utils.db_manager import init_db
from src.utils.log_manager import init_logging
from src.utils.env_constants import HOSTNAME, PORT, RELOAD, LOGLEVEL
from src.routes.v1.root_router import root_router
from src.routes.v1.car_router import car_router
from src.routes.v1.user_router import user_router


app = FastAPI(
    title="EZEV",
    description="This is a backend for an EV comparison tool",
    docs_url="/",
    version="pre-release",
    openapi_url="/api/v1/openapi.json",
)

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_logging()
app.mount("/static", StaticFiles(directory="src/static"), name="static")


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
