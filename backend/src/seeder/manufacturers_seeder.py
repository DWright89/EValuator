from src.models.database import Manufacturers
from loguru import logger

# to run: python -m src.seeder.main


async def create_manufacturers():
    logger.info("creating manufacturers")
    await Manufacturers.create(name="Tesla", website="http://tesla.com")
    await Manufacturers.create(name="Rivian", website="https://rivian.com/")
    await Manufacturers.create(name="Ford", website="https://www.ford.com/")
    await Manufacturers.create(name="Chevrolet", website="https://www.chevrolet.com/")
    await Manufacturers.create(name="Nissan", website="https://www.nissanusa.com/")
    await Manufacturers.create(name="Audi", website="https://www.audiusa.com/")
    await Manufacturers.create(name="Kia", website="https://www.kia.com/us/en")
