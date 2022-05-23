from src.models.database import Manufacturers, Cars, Trims
from loguru import logger


async def create_cars_polestar():
    polestar = await Manufacturers.filter(name="Polestar").first()
    logger.info("Creating cars - Polestar")
    await Cars.create(
        manufacturer_id=polestar.id,
        website="https://www.polestar.com/us/polestar-2/configurator",
        image="polestar2.png",
        make="Polestar",
        model="Polestar 2",
        year=2022,
        cargo=14.3
    )


async def create_trims_polestar():
    polestar2 = await Cars.filter(model="Polestar 2").first()
    logger.info("Creating trims - Polestar")

    await Trims.create(
        car_id=polestar2.id,
        trim="Long Range FWD",
        kwh=78,
        range=270,
        fwd=True,
        rwd=False,
        awd=False,
        acceleration=7,
        horsepower=231,
        torque=243,
        weight=4400,
        mpge=107,
        kwh100mi=31,
        charge240="8",
        price=48400,
        rating=0.0,
    )

    await Trims.create(
        car_id=polestar2.id,
        trim="Long Range AWD",
        kwh=78,
        range=260,
        fwd=False,
        rwd=False,
        awd=True,
        acceleration=4.5,
        horsepower=408,
        torque=487,
        weight=4650,
        mpge=89,
        kwh100mi=38,
        charge240="8",
        price=51900,
        rating=0.0,
    )
