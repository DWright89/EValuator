from fastapi import APIRouter


from src.models.database.Trims import Trims

trims_router = APIRouter(
    prefix="/trims",
    tags=["trims"],
    responses={404: {"description": "Not found"}},
)

# Make this selectively get trims for a specific model


@trims_router.get("/")
async def get_trims():
    return await Trims.all()
