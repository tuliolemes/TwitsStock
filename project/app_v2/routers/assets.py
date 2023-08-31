from fastapi import APIRouter
from project.app_v2.database.database import fetch_data


router = APIRouter()


@router.get("/assets", tags=["assets"])
async def get_assets():
    query = "SELECT id, symbol, name FROM assets"
    result = await fetch_data(router.pool, query)
    return result