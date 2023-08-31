from fastapi import APIRouter
from project.app_v2.database.database import create_pg_pool, fetch_data


router = APIRouter()


@router.get("/user_assets", tags=["user_assets"])
async def get_user_assets():
    query = """
        SELECT ua.user_id, ua.asset_id, ua.quantity, a.symbol
        FROM user_assets ua
        JOIN assets a ON ua.asset_id = a.id
    """
    result = await fetch_data(router.pool, query)
    return result