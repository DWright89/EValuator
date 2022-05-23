from src.models.database import Manufacturers, Cars, Trims
from loguru import logger


async def create_cars_vw():
    vw = await Manufacturers.filter(name="Volkswagen").first()
    logger.info("Creating cars - Volkswagen")

    await Cars.create(
        manufacturer_id=vw.id,
        website="https://www.vw.com/en/models/id-4.html",
        image="vwid4.png",
        make="Volkswagen",
        model="ID.4",
        year=2022,
        cargo=30.3
    )


async def create_trims_vw():
    id4 = await Cars.filter(model="ID.4").first()
    logger.info("Creating trims - Volkswagen")

    await Trims.create(
        car_id=id4.id,
        trim="Pro RWD",
        kwh=82,
        range=280,
        fwd=False,
        rwd=True,
        awd=False,
        acceleration=7.7,
        horsepower=201,
        torque=229,
        weight=4568,
        mpge=112,
        kwh100mi=30,
        charge240="7.5",
        price=42425,
        rating=0.0,
    )

    await Trims.create(
        car_id=id4.id,
        trim="Pro AWD",
        kwh=82,
        range=251,
        fwd=False,
        rwd=False,
        awd=True,
        acceleration=5.7,
        horsepower=295,
        torque=229,
        weight=4824,
        mpge=101,
        kwh100mi=33,
        charge240="7.5",
        price=46105,
        rating=0.0,
    )

    await Trims.create(
        car_id=id4.id,
        trim="Pro S RWD",
        kwh=82,
        range=268,
        fwd=False,
        rwd=True,
        awd=False,
        acceleration=7.7,
        horsepower=201,
        torque=229,
        weight=4,
        mpge=112,
        kwh100mi=30,
        charge240="7.5",
        price=46925,
        rating=0.0,
    )

    await Trims.create(
        car_id=id4.id,
        trim="Pro S AWD",
        kwh=82,
        range=245,
        fwd=False,
        rwd=False,
        awd=True,
        acceleration=5.7,
        horsepower=295,
        torque=229,
        weight=4927,
        mpge=95,
        kwh100mi=35,
        charge240="7.5",
        price=50605,
        rating=0.0,
    )
