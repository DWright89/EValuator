from src.models.database import Manufacturers, Cars, Trims
from loguru import logger

async def create_cars_tesla():
    tesla = await Manufacturers.filter(name="Tesla").first()
    logger.info("Creating cars - Tesla")
    await Cars.create(
        manufacturer_id=tesla.id,
        website="https://www.tesla.com/model3",
        image="teslamodel3.png",
        make="Tesla",
        model="Model 3",
        year=2022,
        cargo=22.9,
    )
    await Cars.create(
        manufacturer_id=tesla.id,
        website="https://www.tesla.com/models",
        image="teslamodels.png",
        make="Tesla",
        model="Model S",
        year=2022,
        cargo=28,
    )
    await Cars.create(
      manufacturer_id=tesla.id,
      website="https://www.tesla.com/modelx",
      image="teslamodelx.png",
      make="Tesla",
      model="Model X",
      year=2022,
      cargo=37.1
    )
    await Cars.create(
      manufacturer_id=tesla.id,
      website="https://www.tesla.com/modely",
      image="teslamodely.png",
      make="Tesla",
      model="Model Y",
      year=2022,
      cargo=30.2
    )


async def create_trims_tesla():
    logger.info("Creating trims - Tesla")
    model_3 = await Cars.filter(model="Model 3").first()
    model_s = await Cars.filter(model="Model S").first()
    model_x = await Cars.filter(model="Model X").first()
    model_y = await Cars.filter(model="Model Y").first()
    #model 3
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
        weight=3552,
        mpge=132.0,
        kwh100mi=25,
        charge120="",
        charge240="8.5",
        chargeport="",
        price=46990,
        rating=8.5,
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
        weight=4072,
        mpge=134,
        kwh100mi=25,
        charge120="",
        charge240="10.5",
        chargeport="",
        price=54490,
        rating=8.5,
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
        weight=4072,
        mpge=134,
        kwh100mi=30,
        charge120="",
        charge240="10.5",
        chargeport="",
        price=61990,
        rating=8.5,
    )
    #model s
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
        weight=4561,
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
        weight=4766,
        mpge=116,
        kwh100mi=29,
        charge120="",
        charge240="9",
        price=140490,
        rating=9.0,
    )
    #model x
    await Trims.create(
      car_id=model_x.id,
        trim="Long Range",
        kwh=100,
        range=332,
        fwd=False,
        rwd=False,
        awd=True,
        acceleration=3.8,
        horsepower=670,
        torque=713,
        weight=5183,
        mpge=102,
        kwh100mi=33,
        charge120="",
        charge240="14",
        price=120490,
        rating=9.0,

    )
    await Trims.create(
      car_id=model_x.id,
        trim="Plaid - 20in wheels",
        kwh=100,
        range=333,
        fwd=False,
        rwd=False,
        awd=True,
        acceleration=2.5,
        horsepower=1020,
        torque=1050,
        weight=5390,
        mpge=98,
        kwh100mi=34,
        charge120="",
        charge240="14",
        price=138490,
        rating=6.5,
    )
    await Trims.create(
      car_id=model_x.id,
        trim="Plaid - 22in wheels",
        kwh=100,
        range=311,
        fwd=False,
        rwd=False,
        awd=True,
        acceleration=2.5,
        horsepower=1020,
        torque=1050,
        weight=5390,
        mpge=91,
        kwh100mi=37,
        charge120="",
        charge240="14",
        price=144490,
        rating=6.5,
    )
    #model y
    await Trims.create(
      car_id=model_y.id,
      trim="Long Range",
      kwh=80,
      range=318,
      fwd=False,
      rwd=False,
      awd=True,
      acceleration=4.8,
      horsepower=447,
      torque=376,
      weight=4416,
      mpge=122,
      kwh100mi=28,
      charge120="",
      charge240="11.5",
      price=64990,
      rating=7.5
    )
    await Trims.create(
      car_id=model_y.id,
      trim="Long Range Performance",
      kwh=80,
      range=303,
      fwd=False,
      rwd=False,
      awd=True,
      acceleration=3.5,
      horsepower=580,
      torque=481,
      weight=4416,
      mpge=111,
      kwh100mi=30,
      charge120="",
      charge240="11.8",
      price=67990,
      rating=7.5
    )
   