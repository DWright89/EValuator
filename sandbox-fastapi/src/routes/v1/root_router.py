from fastapi import APIRouter
from src.routes.v1 import user_router, car_router

root_router = APIRouter()
root_router.include_router(user_router.user_router, prefix="/v1", tags=["V1"])
root_router.include_router(car_router.car_router, prefix="/v1", tags=["V1"])


@root_router.get("/root")
def root():
    """
    This is an example router for examples!!!!
    """
    return {"hello": "world"}
