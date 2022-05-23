from src.models.database import Manufacturers, Cars, Trims
from loguru import logger


async def create_cars_bmw():
    bmw = await Manufacturers.filter(name="BMW").first()
    logger.info("Creating cars - BMW")
    await Cars.create(
        manufacturer_id=bmw.id,
        website="https://www.bmwusa.com/vehicles/all-electric/ix/sports-activity-vehicle/build-your-own.html",
        image="bmwix50.png",
        make="BMW",
        model="iX",
        year=2022,
        cargo=35.5
    )

    await Cars.create(
        manufacturer_id=bmw.id,
        website="https://www.bmwusa.com/vehicles/all-electric/i4/gran-coupe/build-your-own.html",
        image="bmwi4edrive40.png",
        make="BMW",
        model="i4",
        year=2022,
        cargo=10
    )


async def create_trims_bmw():
    ix50 = await Cars.filter(model="iX").first()
    i440 = await Cars.filter(model="i4").first()
    logger.info("Creating trims - BMW")

    await Trims.create(
        car_id=ix50.id,
        trim="xDrive50",
        kwh=111.5,
        range=324,
        fwd=False,
        rwd=False,
        awd=True,
        acceleration=4.4,
        horsepower=516,
        torque=564,
        weight=5659,
        mpge=86,
        kwh100mi=39,
        charge240="8",
        price=83200,
        rating=0.0,
    )

    await Trims.create(
        car_id=i440.id,
        trim="eDrive40",
        kwh=83.9,
        range=324,
        fwd=False,
        rwd=True,
        awd=False,
        acceleration=5.5,
        horsepower=335,
        torque=317,
        weight=4680,
        mpge=109,
        kwh100mi=31,
        charge240="8",
        price=55400,
        rating=0.0,
    )
