from fastapi import APIRouter
from pydantic import BaseModel
from loguru import logger


from src.models.database.Manufacturers import Manufacturers
from src.models.api.Manufacturer import OneManufacturer, ManufacturerList

manufacturers_router = APIRouter(
    prefix="/manufacturers",
    tags=["manufacturers"],
    responses={404: {"description": "Not found"}},
)


class ManufacturerModel(BaseModel):
    name: str = "Tesla"


@manufacturers_router.get("/")
async def get_manufacturers():
    """
    API endpoint to return every manufacturer.
    """
    return await Manufacturers.all()


@manufacturers_router.get("/{name}")
async def get_one_manufacturer(name: str):
    """
    API endpoint to return one manufacturer.
    """
    one_manufacturer = await Manufacturers.filter(name=name).first()
    return one_manufacturer
