from src.models.database import Manufacturers, Cars, Trims
from loguru import logger


async def create_cars_mercedes():
    mercedes = await Manufacturers.filter(name="Mercedes").first()
    logger.info("Creating cars - Mercedes")

    await Cars.create(
        manufacturer_id=mercedes.id,
        website="https://www.mbusa.com/en/vehicles/build/eqs/sedan",
        image="mercedeseqs.png",
        make="Mercedes",
        model="EQS",
        year=2022,
        cargo=22
    )


async def create_trims_mercedes():
    eqs = await Cars.filter(model="EQS").first()
    logger.info("Creating trims - Mercedes")

    await Trims.create(
        car_id=eqs.id,
        trim="450+",
        kwh=107.8,
        range=350,
        fwd=False,
        rwd=True,
        awd=False,
        acceleration=5.9,
        horsepower=329,
        torque=417,
        weight=5597,
        mpge=97,
        kwh100mi=35,
        charge240="8",
        price=102310,
        rating=0.0,
    )

    await Trims.create(
        car_id=eqs.id,
        trim="540 4MATIC",
        kwh=107.8,
        range=340,
        fwd=False,
        rwd=False,
        awd=True,
        acceleration=4.1,
        horsepower=516,
        torque=631,
        weight=5888,
        mpge=95,
        kwh100mi=36,
        charge240="8",
        price=125900,
        rating=0.0,
    )
