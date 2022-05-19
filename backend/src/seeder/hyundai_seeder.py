from src.models.database import Manufacturers, Cars, Trims
from loguru import logger


async def create_cars_hyundai():
    hyundai = await Manufacturers.filter(name="Hyundai").first()
    logger.info("Creating cars - Hyundai")
    await Cars.create(
        manufacturer_id=hyundai.id,
        website="https://www.hyundaiusa.com/us/en/vehicles/ioniq-5",
        image="hyundaiioniq5.png",
        make="Hyundai",
        model="Ioniq 5",
        year=2022,
        cargo=27
    )

    await Cars.create(
        manufacturer_id=hyundai.id,
        website="https://www.hyundaiusa.com/us/en/vehicles/kona-electric",
        image="hyundaikonaelectric.png",
        make="Hyundai",
        model="Kona Electric",
        year=2022,
        cargo=45.8
    )

async def create_trims_hyundai():
    ioniq = await Cars.filter(model="Ioniq 5").first()
    kona = await Cars.filter(model="Kona Electric").first()

    await Trims.create(
        car_id=ioniq.id,
        trim="SE RWD",
        kwh=77.4,
        range=303,
        fwd=False,
        rwd=True,
        awd=False,
        acceleration=7.4,
        horsepower=225,
        torque=218,
        weight=4200,
        mpge=132,
        kwh100mi=30,
        charge240="8.5",
        price=45245,
        rating=0.0,
    )
    await Trims.create(
        car_id=ioniq.id,
        trim="SEL RWD",
        kwh=77.4,
        range=303,
        fwd=False,
        rwd=True,
        awd=False,
        acceleration=7.4,
        horsepower=225,
        torque=218,
        weight=4200,
        mpge=132,
        kwh100mi=30,
        charge240="8.5",
        price=48495,
        rating=0.0,
    )
    await Trims.create(
        car_id=ioniq.id,
        trim="Limited RWD",
        kwh=77.4,
        range=303,
        fwd=False,
        rwd=True,
        awd=False,
        acceleration=7.4,
        horsepower=225,
        torque=218,
        weight=4200,
        mpge=132,
        kwh100mi=30,
        charge240="8.5",
        price=53345,
        rating=0.0,
    )

    await Trims.create(
        car_id=ioniq.id,
        trim="SE AWD",
        kwh=77.4,
        range=256,
        fwd=False,
        rwd=False,
        awd=True,
        acceleration=4.4,
        horsepower=320,
        torque=446,
        weight=4660,
        mpge=127,
        kwh100mi=34,
        charge240="8.5",
        price=48745,
        rating=0.0,
    )
    await Trims.create(
        car_id=ioniq.id,
        trim="SEL AWD",
        kwh=77.4,
        range=256,
        fwd=False,
        rwd=False,
        awd=True,
        acceleration=4.4,
        horsepower=320,
        torque=446,
        weight=4660,
        mpge=127,
        kwh100mi=34,
        charge240="8.5",
        price=51995,
        rating=0.0,
    )
    await Trims.create(
        car_id=ioniq.id,
        trim="Limited AWD",
        kwh=77.4,
        range=256,
        fwd=False,
        rwd=False,
        awd=True,
        acceleration=4.4,
        horsepower=320,
        torque=446,
        weight=4660,
        mpge=127,
        kwh100mi=34,
        charge240="8.5",
        price=56245,
        rating=0.0,
    )

    await Trims.create(
        car_id=kona.id,
        trim="SEL",
        kwh=64,
        range=258,
        fwd=True,
        rwd=False,
        awd=False,
        acceleration=6.6,
        horsepower=201,
        torque=291,
        weight=3715,
        mpge=120,
        kwh100mi=28,
        charge240="8.5",
        price=35245,
        rating=0.0,
    )

    await Trims.create(
        car_id=kona.id,
        trim="Limited",
        kwh=64,
        range=258,
        fwd=True,
        rwd=False,
        awd=False,
        acceleration=6.6,
        horsepower=201,
        torque=291,
        weight=3715,
        mpge=120,
        kwh100mi=28,
        charge240="8.5",
        price=42500,
        rating=0.0,
    )
