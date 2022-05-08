from src.models.database import Manufacturers, Cars, Trims
from loguru import logger


async def create_cars_chevy():
    chevy = await Manufacturers.filter(name="Chevrolet").first()
    logger.info("Creating cars - Chevy")
    await Cars.create(
        manufacturer_id=chevy.id,
        website="https://www.chevrolet.com/electric/bolt-ev",
        image="chevyboltev.png",
        make="Chevrolet",
        model="Bolt EV",
        year=2022,
        cargo=17,
    )
    await Cars.create(
        manufacturer_id=chevy.id,
        website="https://www.chevrolet.com/electric/bolt-euv",
        image="chevybolteuv.png",
        make="Chevrolet",
        model="Bolt EUV",
        year=2022,
        cargo=11.9,
    )


async def create_trims_chevy():
    bolt_ev = await Cars.filter(model="Bolt EV").first()
    bolt_euv = await Cars.filter(model="Bolt EUV").first()
    # Bolt EV
    await Trims.create(
        car_id=bolt_ev.id,
        trim="1LT",
        kwh=66,
        range=289,
        fwd=True,
        rwd=False,
        awd=False,
        acceleration=6.5,
        horsepower=200,
        torque=266,
        weight=3589,
        mpge=120,
        kwh100mi=29,
        charge120="",
        charge240="13",
        price=31500,
        rating=8.0,
    )
    await Trims.create(
        car_id=bolt_ev.id,
        trim="2LT",
        kwh=66,
        range=289,
        fwd=True,
        rwd=False,
        awd=False,
        acceleration=6.5,
        horsepower=200,
        torque=266,
        weight=3589,
        mpge=120,
        kwh100mi=28,
        charge120="",
        charge240="7.5",
        price=35500,
        rating=8.0,
    )
    # Bolt EUV
    await Trims.create(
        car_id=bolt_euv.id,
        trim="LT",
        kwh=65,
        range=241,
        fwd=True,
        rwd=False,
        awd=False,
        acceleration=7.0,
        horsepower=200,
        torque=266,
        weight=3680,
        mpge=115,
        kwh100mi=25,
        charge120="",
        charge240="7.5",
        price=34495,
        rating=8.0,
    )
    await Trims.create(
        car_id=bolt_euv.id,
        trim="Premier",
        kwh=65,
        range=289,
        fwd=True,
        rwd=False,
        awd=False,
        acceleration=7.0,
        horsepower=200,
        torque=266,
        weight=3680,
        mpge=115,
        kwh100mi=25,
        charge120="",
        charge240="7.5",
        price=38995,
        rating=8.0,
    )
