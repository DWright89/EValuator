from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from loguru import logger
from typing import List

from src.models.database.Cars import Cars
from src.models.database.Manufacturers import Manufacturers

# router setting
car_router = APIRouter(
    prefix="/cars",
    tags=["cars"],
    responses={404: {"description": "Not found"}},
)


class CarModel(BaseModel):
    id: int 
    user_id: int
    manufacturer_id: int
    model: str
    image: str
    make: str
    model: str
    year: int
    cargo: float



@car_router.post("/")
async def create_car(request: CarModel):
    """
    Api endpoint to create cars
    """
    car = await Cars.create(**request.dict(exclude_unset=True))
    return await car


@car_router.get("/")
async def get_cars():
    """
    API endpoint to get every car
    """
    logger.info("Something is happening")
    return await Cars.all()


class ManufacturerResponse(BaseModel):
    cars: List[CarModel]


@car_router.get("/{manufacturer}")
async def get_cars_by_manufacturer(manufacturer: str):
    """
    API endpoint to get every car from a given manufacturer
    """
    car_list = []
    manufacturer_id = await Manufacturers.filter(name__iexact=manufacturer).first()    
    car_list.extend(await Cars.filter(manufacturer_id=manufacturer_id.id))
    return car_list


@car_router.get("/{make}/{model}")
async def get_one_car(make: str, model: str):
    """
    API endpoint to get one car by make and model.
    Make should be supplied from a Manufactuerer object, eventually.
    """
    one_car = await Cars.filter(make=make, model=model).first()
    return one_car
