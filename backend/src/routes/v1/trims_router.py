from fastapi import APIRouter
from loguru import logger
from typing import List

from src.models.database.Trims import Trims, Trims_Response
from src.models.database.Cars import Cars
from src.models.database.Manufacturers import Manufacturers


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
    #all_trims = await Trims_Response.from_queryset(Trims.all())
    all_trims = await Trims.all()
    all_cars = []
    for trim in all_trims:
        car = await Cars.filter(id=trim.car_id).first()
        manufacturer = await Manufacturers.filter(id=car.manufacturer_id).first()
        whole_car = {
            "manufacturer": manufacturer,
            "model": car,
            "trim": trim
        }
        one_car = [manufacturer, car, trim]
        all_cars.append(whole_car)

    return all_cars


@trims_router.get("/{make}/{model}")
async def get_trims_by_car(make: str, model: str):
    """
    API endpoint to get every trim level for one car.
    Make and Model should come from a Manufactuerer and Car object, respectively.
    """
    car = await Cars.filter(make=make, model=model).first()
    trim = await Trims_Response.from_queryset(Trims.filter(car_id=car.id))
    return trim
