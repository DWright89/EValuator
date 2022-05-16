# takes in two trims, gets the whole car, returns a list of both cars
from src.models.database.Manufacturers import Manufacturers
from src.models.database.Cars import Cars
from src.models.database.Trims import Trims, Trims_Response


async def get_full_car(trim_id: int):

    trim = await Trims.filter(id=trim_id).first()
    car = await Cars.filter(id=trim.car_id).first()
    manufacturer = await Manufacturers.filter(id=car.manufacturer_id).first()
    return [manufacturer, car, trim]


async def get_comparison(trim1: int, trim2: int):
    first_car = await get_full_car(trim1)
    second_car = await get_full_car(trim2)
    return [first_car, second_car]
