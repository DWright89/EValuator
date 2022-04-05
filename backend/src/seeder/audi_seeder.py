from src.models.database import Manufacturers, Cars, Trims
from loguru import logger

async def create_cars_audi():
  audi = await Manufacturers.filter(name="Audi").first()
  logger.info("Creating cars - Audi")
  await Cars.create(
    manufacturer_id=audi.id,
    website="https://www.audiusa.com/us/web/en/models/q4/q4-e-tron/2022/overview.html",
    image="audiq4.png",
    make="Audi",
    model="Q4",
    year=2022,
    cargo=53.1
  )
  await Cars.create(
    manufacturer_id=audi.id,
    website="https://www.audiusa.com/us/web/en/models/q4/q4-sportback-e-tron/2022/overview.html",
    image="audiq4sportback.png",
    make="Audi",
    model="Q4 Sportback",
    year=2022,
    cargo=53.1
  )
  await Cars.create(
    manufacturer_id=audi.id,
    website="https://www.audiusa.com/us/web/en/models/e-tron/e-tron/2022/overview.html",
    image="audietron.png",
    make="Audi",
    model="e-Tron S",
    year=2022,
    cargo=28.5
  )
  await Cars.create(
    manufacturer_id=audi.id,
    website="https://www.audiusa.com/us/web/en/models/e-tron/e-tron-gt/2022/overview.html",
    image="audietrongt.png",
    make="Audi",
    model="e-Tron GT",
    year=2022,
    cargo=9.2
  )

async def create_trims_audi():
  q4 = await Cars.filter(model="Q4").first()
  sportback = await Cars.filter(model="Q4 Sportback").first()
  etron = await Cars.filter(model="e-Tron S").first()
  gt = await Cars.filter(model="e-Tron GT").first()
  logger.info("Creating trims - Audi")
  await Trims.create(
    car_id=q4.id,
    trim="Premium",
    kwh=82,
    range=241,
    fwd=False,
    rwd=False,
    awd=True,
    acceleration=5.8,
    horsepower=295,
    torque=340,
    weight=4870,
    mpge=95.0,
    kwh100mi=36,
    charge120="",
    charge240="12",
    chargeport="",
    price=51095,
    rating=0.0,
  )
  await Trims.create(
    car_id=q4.id,
    trim="Chronos",
    kwh=82,
    range=222,
    fwd=False,
    rwd=False,
    awd=True,
    acceleration=5.5,
    horsepower=402,
    torque=490,
    weight=4870,
    mpge=95.0,
    kwh100mi=36,
    charge120="",
    charge240="12",
    chargeport="",
    price=85190,
    rating=0.0,
  )

  await Trims.create(
    car_id=sportback.id,
    trim="Premium",
    kwh=95,
    range=218,
    fwd=False,
    rwd=False,
    awd=True,
    acceleration=5.5,
    horsepower=402,
    torque=490,
    weight=5754,
    mpge=75,
    kwh100mi=45,
    charge120="",
    charge240="10.5",
    chargeport="",
    price=69100,
    rating=0.0
  )
  await Trims.create(
    car_id=etron.id,
    trim="Premium Plus",
    kwh=95,
    range=208,
    fwd=False,
    rwd=False,
    awd=True,
    acceleration=4.3,
    horsepower=496,
    torque=717,
    weight=6085,
    mpge=78,
    kwh100mi=43,
    charge120="",
    charge240="10.5",
    chargeport="",
    price=84800,
    rating=0.0
  )
  await Trims.create(
    car_id=gt.id,
    trim="Premium Plus",
    kwh=93,
    range=238,
    fwd=False,
    rwd=False,
    awd=True,
    acceleration=3.9,
    horsepower=522,
    torque=472,
    weight=5060,
    mpge=82,
    kwh100mi=41,
    charge240="10.5",
    price=102400,
    rating=0.0
  )
  await Trims.create(
    car_id=gt.id,
    trim="e-Tron GT quattro",
    kwh=93,
    range=238,
    fwd=False,
    rwd=False,
    awd=True,
    acceleration=3.9,
    horsepower=637,
    torque=612,
    weight=5060,
    mpge=82,
    kwh100mi=41,
    charge240="10.5",
    price=144490,
    rating=0.0
  )