from src.models.database import Manufacturers, Cars, Packages
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
        image="",
        make="Tesla",
        model="3",
        year=2022,
        cargo=22.9,
    )
    await Cars.create(
        manufacturer_id=tesla.id,
        website="https://www.tesla.com/models",
        image="",
        make="Tesla",
        model="S",
        year=2022,
        cargo=64.6,
    )


async def create_packages():
    logger.info("creating packages")
    model_3 = await Cars.filter(model="3").first()
    await Packages.create(
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
    await Packages.create(
        car_id=model_3.id,
        trim="Long Range",
        kwh=75,
        range=358,
        fwd=False,
        rwd=False,
        awd=True,
        acceleration=4.2,
        horsepower=449,
        torque=3471,
        mpge=134,
        kwh100mi=25,
        charge120="",
        charge240="10.5",
        chargeport="",
        price=54490,
        rating=0.0,
    )
