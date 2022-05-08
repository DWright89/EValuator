from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from loguru import logger

from src.models.database.Trims import Trims

from src.controllers.comparison_controller import get_comparison


comparisons_router = APIRouter(prefix="/comparisons", tags=["trims"], responses={404: {"description": "Not Found"}})


class OneComparison(BaseModel):
    trim_one_id: int
    trim_two_id: int


@comparisons_router.get("/{trim1}/{trim2}")
async def return_comparison(trim1: int, trim2: int):
    """
    API endpoint to retreive two trims and return the whole car
    """
    logger.info("Hit the comparison router ", trim1, trim2)
    return await get_comparison(trim1, trim2)
