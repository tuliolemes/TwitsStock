from fastapi import APIRouter
from project.app_v2.database.database import fetch_data, get_pool


router = APIRouter()


@router.get("/assets", tags=["assets"])
async def get_assets():
    pool = await get_pool()
    query = "SELECT id, symbol, name FROM assets"
    result = await fetch_data(pool, query)
    return result