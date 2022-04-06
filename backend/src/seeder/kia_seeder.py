from select import KQ_FILTER_SIGNAL
from src.models.database import Manufacturers, Cars, Trims
from loguru import logger

async def create_cars_kia():
  kia = await Manufacturers.filter(name="Kia").first()
  logger.info("Creating cars - Kia")
  await Cars.create(
    manufacturer_id=kia.id,
    website="https://www.kia.com/us/en/ev6",
    image="kiaev.png",
    make="Kia",
    model="EV6",
    year=2022,
    cargo=24.4
  )

  async def create_trims_kia():
    ev6 = await Cars.filter(model="EV6").first()
    logger.info("Creating trims - Kia")
    #EV6
    await Trims.create(
      car_id=ev6.id,
      trim="Light",
      kwh=58,
      range=232,
      fwd=False,
      rwd=True,
      awd=False,
      acceleration=5.8, #FIND THIS OUT
      horsepower=167,
      torque=258,
      weight=3984,
      mpge=117.0,
      kwh100mi=29,
      charge120="",
      charge240="6.3",
      chargeport="",
      price=40900,
      rating=8.0,
  )