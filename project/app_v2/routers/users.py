from fastapi import APIRouter
from project.app_v2.database.database import get_pool, fetch_data


router = APIRouter()


@router.get("/users", tags=["users"])
async def get_users():
    pool = await get_pool()
    query = "SELECT id, username FROM users"
    result = await fetch_data(pool, query)
    return result