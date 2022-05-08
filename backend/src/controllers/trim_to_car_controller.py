from src.models.database.Manufacturers import Manufacturers
from src.models.database.Cars import Cars


async def get_full_car_from_trim(trim_fk: int):

    car = await Cars.filter(id=trim_fk).first()
    manufacturer = await Manufacturers.filter(id=car.manufacturer_id).first()
    return [manufacturer, car]
