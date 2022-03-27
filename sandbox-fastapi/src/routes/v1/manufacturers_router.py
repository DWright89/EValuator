from fastapi import APIRouter


from src.models.database.Manufacturers import Manufacturers

manufacturers_router = APIRouter(
    prefix="/manufacturers",
    tags=["manufacturers"],
    responses={404: {"description": "Not found"}},
)


@manufacturers_router.get("/")
async def get_manufacturers():
    return await Manufacturers.all()
