from src.models.database import Manufacturers, Cars, Trims
from loguru import logger


async def create_cars_toyota():
    toyota = await Manufacturers.filter(name="Toyota").first()
    logger.info("Creating cars - Toyota")
    await Cars.create(
        manufacturer_id=toyota.id,
        website="https://www.toyota.com/bz4x/2023/",
        image="toyotabz4x.png",
        make="Toyota",
        model="bZ4x",
        year=2023,
        cargo=27.7,
    )


async def create_trims_toyota():
    logger.info("Creating trims - Toyota")
    bz4x = await Cars.filter(model="bZ4x").first()
    await Trims.create(
        car_id=bz4x.id,
        trim="XLE FWD",
        kwh=72.8,
        range=242,
        fwd=True,
        rwd=False,
        awd=False,
        acceleration=8.4,
        horsepower=201,
        torque=196,
        weight=4233,
        mpge=120.0,
        kwh100mi=30,
        charge120="",
        charge240="9",
        chargeport="",
        price=42000,
        rating=7,
    )

    await Trims.create(
        car_id=bz4x.id,
        trim="XLE AWD",
        kwh=72.8,
        range=228,
        fwd=False,
        rwd=False,
        awd=True,
        acceleration=7.7,
        horsepower=214,
        torque=248,
        weight=4453,
        mpge=120.0,
        kwh100mi=30,
        charge120="",
        charge240="9",
        chargeport="",
        price=44080,
        rating=7,
    )

    await Trims.create(
        car_id=bz4x.id,
        trim="Limited FWD",
        kwh=72.8,
        range=242,
        fwd=True,
        rwd=False,
        awd=False,
        acceleration=8.4,
        horsepower=201,
        torque=196,
        weight=4233,
        mpge=120.0,
        kwh100mi=30,
        charge120="",
        charge240="9",
        chargeport="",
        price=46700,
        rating=7,
    )

    await Trims.create(
        car_id=bz4x.id,
        trim="Limited AWD",
        kwh=72.8,
        range=222,
        fwd=False,
        rwd=False,
        awd=True,
        acceleration=7.7,
        horsepower=214,
        torque=248,
        weight=4453,
        mpge=120.0,
        kwh100mi=30,
        charge120="",
        charge240="9",
        chargeport="",
        price=48780,
        rating=7,
    )
