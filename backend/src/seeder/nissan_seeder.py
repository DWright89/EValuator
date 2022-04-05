from src.models.database import Manufacturers, Cars, Trims
from loguru import logger

async def create_cars_nissan():
  nissan = await Manufacturers.filter(name="Nissan").first()
  logger.info("Creating cars - Nissan")
  await Cars.create(
    manufacturer_id=nissan.id,
    website="https://www.nissanusa.com/vehicles/electric-cars/leaf.html",
    image="nissanleaf.png",
    make="Nissan",
    model="Leaf",
    year=2022,
    cargo=23.6
  )

async def create_trims_nissan():
  leaf = await Cars.filter(model="Leaf").first()
  logger.info("Creating cars - Nissan")
  await Trims.create( 
    car_id=leaf.id,
    trim="S",
    kwh=40,
    range=247,
    fwd=True,
    rwd=False,
    awd=False,
    acceleration=7.5,
    horsepower=147,
    torque=236,
    weight=3480,
    mpge=111,
    kwh100mi=30,
    charge120="",
    charge240="8",
    chargeport="",
    price=27400,
    rating=6.5
    )
  await Trims.create(
    car_id=leaf.id,
    trim="SV",
    kwh=40,
    range=247,
    fwd=True,
    rwd=False,
    awd=False,
    acceleration=7.5,
    horsepower=147,
    torque=236,
    weight=3480,
    mpge=111,
    kwh100mi=30,
    charge120="",
    charge240="8",
    chargeport="",
    price=28800,
    rating=6.5,
  )
  await Trims.create(
    car_id=leaf.id,
    trim="S Plus",
    kwh=62,
    range=247,
    fwd=True,
    rwd=False,
    awd=False,
    acceleration=7.4,
    horsepower=214,
    torque=317,
    weight=3620,
    mpge=108,
    kwh100mi=31,
    charge120="",
    charge240="11",
    chargeport="",
    price=32400,
    rating=6.5,
  )
  await Trims.create(
    car_id=leaf.id,
    trim="SV Plus",
    kwh=62,
    range=247,
    fwd=True,
    rwd=False,
    awd=False,
    acceleration=7.4,
    horsepower=214,
    torque=317,
    weight=3620,
    mpge=108,
    kwh100mi=31,
    charge120="",
    charge240="11",
    chargeport="",
    price=35400,
    rating=6.5,
  )
  await Trims.create(
    car_id=leaf.id,
    trim="SL Plus",
    kwh=62,
    range=214,
    fwd=True,
    rwd=False,
    awd=False,
    acceleration=7.4,
    horsepower=266,
    torque=317,
    weight=3620,
    mpge=108,
    kwh100mi=31,
    charge120="",
    charge240="11",
    chargeport="",
    price=37400,
    rating=6.5,
  )