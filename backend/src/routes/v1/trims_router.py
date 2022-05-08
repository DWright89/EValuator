from fastapi import APIRouter
from loguru import logger

from src.models.database.Trims import Trims, Trims_Response
from src.models.database.Cars import Cars


trims_router = APIRouter(
    prefix="/trims",
    tags=["trims"],
    responses={404: {"description": "Not found"}},
)

# Make this selectively get trims for a specific model


@trims_router.get("/")
async def get_all_trims():
    """
    API endpoint to return every trim for every car
    """
    all_trims = await Trims_Response.from_queryset(Trims.all())

    for trim in all_trims:
        logger.info(trim)
    return all_trims


@trims_router.get("/{make}/{model}")
async def get_trims_by_car(make: str, model: str):
    """
    API endpoint to get every trim level for one car.
    Make and Model should come from a Manufactuerer and Car object, respectively.
    """
    car = await Cars.filter(make=make, model=model).first()
    trim = await Trims_Response.from_queryset(Trims.filter(car_id=car.id))
    return trim
