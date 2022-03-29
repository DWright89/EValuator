from fastapi import APIRouter
from pydantic import BaseModel


from src.models.database.Cars import Cars

# router setting
car_router = APIRouter(
    prefix="/cars",
    tags=["cars"],
    responses={404: {"description": "Not found"}},
)


class CarModel(BaseModel):
    user_id: int = 1
    model: str = "altima"


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

    return await Cars.all()


@car_router.get("/{make}/{model}")
async def get_one_car(make: str, model: str):
    """
    API endpoint to get one car by make and model.
    Make should be supplied from a Manufactuerer object, eventually.
    """
    one_car = await Cars.filter(make=make, model=model).first()
    return one_car
