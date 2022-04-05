from src.models.database import Manufacturers, Cars, Trims
from loguru import logger

async def create_cars_ford():
  ford = await Manufacturers.filter(name="Ford").first()
  logger.info("Creating cars - Ford")
  await Cars.create(
    manufacturer_id=ford.id,
    website="https://www.ford.com/suvs/mach-e/",
    image="fordmustangmache.png",
    make="Ford",
    model="Mustang Mach-E",
    year=2022,
    cargo=27.9,
  )

async def create_trims_ford():
  mach_e = await Cars.filter(model="Mustang Mach-E").first()
  logger.info("Creating cars - Ford")
  #mach e
  await Trims.create(
    car_id=mach_e.id,
    trim="Select RWD",
    kwh=70,
    range=247,
    fwd=False,
    rwd=True,
    awd=False,
    acceleration=5.8,
    horsepower=266,
    torque=317,
    weight=3552,
    mpge=103.0,
    kwh100mi=33,
    charge120="",
    charge240="8.1",
    chargeport="",
    price=43895,
    rating=9.5,
  )
  await Trims.create(
    car_id=mach_e.id,
    trim="Select AWD",
    kwh=70,
    range=224,
    fwd=False,
    rwd=False,
    awd=True,
    acceleration=5.2,
    horsepower=266,
    torque=428,
    weight=3552,
    mpge=93.0,
    kwh100mi=36,
    charge120="",
    charge240="8",
    chargeport="",
    price=46595,
    rating=9.5,
  )
  await Trims.create(
    car_id=mach_e.id,
    trim="GT",
    kwh=91,
    range=270,
    fwd=False,
    rwd=False,
    awd=True,
    acceleration=3.8,
    horsepower=480,
    torque=600,
    weight=3552,
    mpge=84.0,
    kwh100mi=40,
    charge120="",
    charge240="10.3",
    chargeport="",
    price=61995,
    rating=9.5,
  )
  await Trims.create(
    car_id=mach_e.id,
    trim="GT Performance",
    kwh=91,
    range=260,
    fwd=False,
    rwd=False,
    awd=True,
    acceleration=5.8,
    horsepower=480,
    torque=634,
    weight=3552,
    mpge=82.0,
    kwh100mi=41,
    charge120="",
    charge240="10.1",
    chargeport="",
    price=67995,
    rating=9.5,
  )