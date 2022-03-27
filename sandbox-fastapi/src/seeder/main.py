from tortoise import Tortoise, run_async
from src.utils.env_constants import DATABASE_URI, MODELS_PATH
from src.seeder.seed_data import create_manufacturers, create_cars, create_packages


async def seed():
    await Tortoise.init(db_url=DATABASE_URI, modules={"models": [MODELS_PATH]})
    await create_manufacturers()
    await create_cars()
    await create_packages()


if __name__ == "__main__":
    run_async(seed())
