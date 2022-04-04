from src.models.database import Manufacturers, Cars, Trims
from loguru import logger

# to run: python -m src.seeder.main


async def create_manufacturers():
    logger.info("creating manufacturers")
    await Manufacturers.create(name="Tesla", website="http://tesla.com")
    await Manufacturers.create(name="Rivian", website="https://rivian.com/")
    await Manufacturers.create(name="Ford", website="https://www.ford.com/")
    await Manufacturers.create(name="Chevrolet", website="https://www.chevrolet.com/")
    await Manufacturers.create(name="GMC", website="https://www.gmc.com/")


async def create_cars():
    tesla = await Manufacturers.filter(name="Tesla").first()
    logger.info("creating cars")
    await Cars.create(
        manufacturer_id=tesla.id,
        website="https://www.tesla.com/model3",
        image="https://i.imgur.com/byHPGhc.png",
        make="Tesla",
        model="3",
        year=2022,
        cargo=22.9,
    )
    await Cars.create(
        manufacturer_id=tesla.id,
        website="https://www.tesla.com/models",
        image="https://i.imgur.com/hEtlu7T.png",
        make="Tesla",
        model="S",
        year=2022,
        cargo=28,
    )


async def create_trims():
    logger.info("creating trims")
    model_3 = await Cars.filter(model="3").first()
    model_s = await Cars.filter(model="S").first()
    await Trims.create(
        car_id=model_3.id,
        trim="Base",
        kwh=54,
        range=272,
        fwd=False,
        rwd=True,
        awd=False,
        acceleration=5.8,
        horsepower=283,
        torque=302,
        mpge=132.0,
        kwh100mi=25,
        charge120="",
        charge240="8.5",
        chargeport="",
        price=46990,
        rating=0.0,
    )
    await Trims.create(
        car_id=model_3.id,
        trim="Long Range",
        kwh=75,
        range=358,
        fwd=False,
        rwd=False,
        awd=True,
        acceleration=4.2,
        horsepower=449,
        torque=302,
        mpge=134,
        kwh100mi=25,
        charge120="",
        charge240="10.5",
        chargeport="",
        price=54490,
        rating=0.0,
    )
    await Trims.create(
        car_id=model_3.id,
        trim="Performance",
        kwh=75,
        range=315,
        fwd=False,
        rwd=False,
        awd=True,
        acceleration=3.1,
        horsepower=449,
        torque=471,
        mpge=134,
        kwh100mi=30,
        charge120="",
        charge240="10.5",
        chargeport="",
        price=61990,
        rating=0.0,
    )
    await Trims.create(
        car_id=model_s.id,
        trim="Long Range",
        kwh=95,
        range=405,
        fwd=False,
        rwd=False,
        awd=True,
        acceleration=3.1,
        horsepower=670,
        torque=487,
        mpge=120,
        kwh100mi=28,
        charge120="",
        charge240="9",
        price=104490,
        rating=0.0,
    )
    await Trims.create(
        car_id=model_s.id,
        trim="Plaid",
        kwh=95,
        range=396,
        fwd=False,
        rwd=False,
        awd=True,
        acceleration=1.99,
        horsepower=1020,
        torque=1050,
        mpge=116,
        kwh100mi=29,
        charge120="",
        charge240="9",
        price=140490,
        rating=0.0,
    )
