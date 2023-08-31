from fastapi import APIRouter
from project.app_v2.database.database import get_pool, fetch_data


router = APIRouter()


@router.get("/user_assets", tags=["user_assets"])
async def get_user_assets():
    pool = await get_pool()
    query = """
        SELECT ua.user_id, ua.asset_id, ua.quantity, a.symbol
        FROM user_assets ua
        JOIN assets a ON ua.asset_id = a.id
    """
    result = await fetch_data(pool, query)
    return result