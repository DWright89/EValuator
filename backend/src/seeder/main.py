from tortoise import Tortoise, run_async
from src.utils.env_constants import DATABASE_URI, MODELS_PATH
from src.seeder.manufacturers_seeder import create_manufacturers
from src.seeder.tesla_seeder import create_cars_tesla, create_trims_tesla
from src.seeder.ford_seeder import create_cars_ford, create_trims_ford
from src.seeder.rivian_seeder import create_cars_rivian, create_trims_rivian
from src.seeder.chevy_seeder import create_cars_chevy, create_trims_chevy
from src.seeder.nissan_seeder import create_cars_nissan, create_trims_nissan
from src.seeder.audi_seeder import create_cars_audi, create_trims_audi
from src.seeder.kia_seeder import create_cars_kia, create_trims_kia


async def seed():
    await Tortoise.init(db_url=DATABASE_URI, modules={"models": [MODELS_PATH]})
    await create_manufacturers()
    await create_cars_tesla()
    await create_trims_tesla()
    await create_cars_ford()
    await create_trims_ford()
    await create_cars_rivian()
    await create_trims_rivian()
    await create_cars_chevy()
    await create_trims_chevy()
    await create_cars_nissan()
    await create_trims_nissan()
    await create_cars_audi()
    await create_trims_audi()
    await create_cars_kia()
    await create_trims_kia()    
  


if __name__ == "__main__":
    run_async(seed())
