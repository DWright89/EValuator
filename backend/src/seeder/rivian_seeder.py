from src.models.database import Manufacturers, Cars, Trims
from loguru import logger

async def create_cars_rivian():
  rivian = await Manufacturers.filter(name="Rivian").first()
  logger.info("Creating cars - Rivian")
  await Cars.create(
    manufacturer_id=rivian.id,
    website="https://rivian.com/configurator/r1t",
    image="rivianr1t.png",
    make="Rivian",
    model="R1T",
    year=2022,
    cargo=11.9,
  )
  await Cars.create(
    manufacturer_id=rivian.id,
    website="https://rivian.com/r1s",
    image="rivianr1s.png",
    make="Rivian",
    model="R1S",
    year=2022,
    cargo=69.4
  )

async def create_trims_rivian():
  logger.info("Creating trims - Rivian")
  r1t = await Cars.filter(model="R1T").first()
  r1s = await Cars.filter(model="R1S").first()
  #R1T
  await Trims.create(
    car_id=r1t.id,
    trim="Explore Large",
    kwh=129,
    range=314,
    fwd=False,
    rwd=False,
    awd=True,
    acceleration=3.3,
    horsepower=835,
    torque=908,
    weight=7184,
    mpge=70,
    kwh100mi=48,
    charge120="",
    charge240="13",
    price=79500,
    rating=8.5
    )
  await Trims.create(
    car_id=r1t.id,
    trim="Explore Max",
    kwh=180,
    range=400,
    fwd=False,
    rwd=False,
    awd=True,
    acceleration=3.3,
    horsepower=835,
    torque=908,
    weight=7184,
    mpge=70,
    kwh100mi=48,
    charge120="",
    charge240="13",
    price=89500,
    rating=8.5
    )
  await Trims.create(
    car_id=r1t.id,
    trim="Adventure Large",
    kwh=129,
    range=314,
    fwd=False,
    rwd=False,
    awd=True,
    acceleration=3.3,
    horsepower=835,
    torque=908,
    weight=7184,
    mpge=70,
    kwh100mi=48,
    charge120="",
    charge240="13",
    price=85000,
    rating=8.5
    )
  await Trims.create(
    car_id=r1t.id,
    trim="Adventure Max",
    kwh=180,
    range=400,
    fwd=False,
    rwd=False,
    awd=True,
    acceleration=3.3,
    horsepower=835,
    torque=908,
    weight=7184,
    mpge=70,
    kwh100mi=48,
    charge120="",
    charge240="13",
    price=95000,
    rating=8.5,
    )
    #R1S
  await Trims.create(
    car_id=r1s.id,
    trim="Explore Dual Motor Standard",
    kwh=54.1,
    range=216,
    fwd=False,
    rwd=False,
    awd=True,
    acceleration=4.0,
    horsepower=600,
    torque=600,
    weight=6916,
    mpge=69,
    kwh100mi=49,
    charge120="",
    charge240="13",
    price=72500,
    rating=0.0
    )
  await Trims.create(
    car_id=r1s.id,
    trim="Explore Dual Motor Large",
    kwh=129,
    range=320,
    fwd=False,
    rwd=False,
    awd=True,
    acceleration=4.0,
    horsepower=600,
    torque=600,
    weight=6916,
    mpge=69,
    kwh100mi=49,
    charge120="",
    charge240="13",
    price=78500,
    rating=0.0
  )
  await Trims.create(
    car_id=r1s.id,
    trim="Explore Quad Motor Large",
    kwh=129,
    range=316,
    fwd=False,
    rwd=False,
    awd=True,
    acceleration=3.5,
    horsepower=835,
    torque=908,
    weight=6916,
    mpge=69,
    kwh100mi=49,
    charge120="",
    charge240="13",
    price=84500,
    rating=0.0
    )
