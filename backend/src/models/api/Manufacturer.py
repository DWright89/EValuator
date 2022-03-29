from pydantic import BaseModel
from typing import List


class OneManufacturer(BaseModel):
    name: str = ""
    website: str = ""


class ManufacturerList(BaseModel):
    manufacturers: List[OneManufacturer]
