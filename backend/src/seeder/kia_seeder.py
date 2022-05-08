from select import KQ_FILTER_SIGNAL
from src.models.database import Manufacturers, Cars, Trims
from loguru import logger


async def create_cars_kia():
    kia = await Manufacturers.filter(name="Kia").first()
    logger.info("Creating cars - Kia")
    await Cars.create(
        manufacturer_id=kia.id,
        website="https://www.kia.com/us/en/ev6",
        image="kiaev6.png",
        make="Kia",
        model="EV6",
        year=2022,
        cargo=24.4,
    )
    await Cars.create(
        manufacturer_id=kia.id,
        website="https://www.kia.com/us/en/niro-ev",
        image="kianeroev.png",
        make="Kia",
        model="Niro EV",
        year=2022,
        cargo=53,
    )


async def create_trims_kia():
    ev6 = await Cars.filter(model="EV6").first()
    niro = await Cars.filter(model="Niro EV").first()
    logger.info("Creating trims - Kia")
    # EV6
    await Trims.create(
        car_id=ev6.id,
        trim="Light",
        kwh=58,
        range=232,
        fwd=False,
        rwd=True,
        awd=False,
        acceleration=8.0,
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
    await Trims.create(
        car_id=ev6.id,
        trim="Wind RWD",
        kwh=77.4,
        range=310,
        fwd=False,
        rwd=True,
        awd=False,
        acceleration=7.2,  # finish this
        horsepower=225,
        torque=258,
        weight=4299,
        mpge=117.0,
        kwh100mi=29,
        charge120="",
        charge240="6.3",
        chargeport="",
        price=48215,
        rating=8.0,
    )
    await Trims.create(
        car_id=ev6.id,
        trim="Wind AWD",
        kwh=77.4,
        range=274,
        fwd=False,
        rwd=False,
        awd=True,
        acceleration=5.1,
        horsepower=320,
        torque=446,
        weight=4539,
        mpge=105.0,
        kwh100mi=32,
        charge120="",
        charge240="8.5",
        chargeport="",
        price=52115,
        rating=8.0,
    )
    await Trims.create(
        car_id=ev6.id,
        trim="GT RWD",
        kwh=77.4,
        range=310,
        fwd=False,
        rwd=True,
        awd=False,
        acceleration=5.1,
        horsepower=225,
        torque=258,
        weight=4539,
        mpge=105.0,
        kwh100mi=32,
        charge120="",
        charge240="8.5",
        chargeport="",
        price=52415,
        rating=8.0,
    )
    await Trims.create(
        car_id=ev6.id,
        trim="GT AWD",
        kwh=77.4,
        range=274,
        fwd=False,
        rwd=False,
        awd=True,
        acceleration=5.1,
        horsepower=320,
        torque=446,
        weight=4539,
        mpge=105.0,
        kwh100mi=32,
        charge120="",
        charge240="8.5",
        chargeport="",
        price=55900,
        rating=8.0,
    )
    # Niro
    await Trims.create(
        car_id=niro.id,
        trim="EX",
        kwh=64,
        range=239,
        fwd=True,
        rwd=False,
        awd=False,
        acceleration=6.2,
        horsepower=201,
        torque=291,
        weight=4916,
        mpge=112,
        kwh100mi=30,
        charge240="9.5",
        price=41205,
        rating=8.0,
    )
    await Trims.create(
        car_id=niro.id,
        trim="EX Premium",
        kwh=64,
        range=239,
        fwd=True,
        rwd=False,
        awd=False,
        acceleration=6.2,
        horsepower=201,
        torque=291,
        weight=4916,
        mpge=112,
        kwh100mi=30,
        charge240="9.5",
        price=45865,
        rating=8.0,
    )
