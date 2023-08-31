from fastapi import APIRouter
from project.app_v2.database.database import get_pool, fetch_data

router = APIRouter()
import requests

base_url = "http://localhost:8000"  # Replace with your FastAPI server's address

def get_users():
    print(f"{base_url}/users")
    response = requests.get("http://localhost:8000/users")
    return response.json()

def get_user_assets():
    response = requests.get(f"{base_url}/user_assets")
    return response.json()

def get_assets():
    response = requests.get(f"{base_url}/assets")
    return response.json()

def combine_data():
    users = get_users()
    print(users)
    user_assets = get_user_assets()
    assets = get_assets()

    combined_data = []

    for user in users:
        user_id = user["id"]
        user_name = user["username"]
        
        user_asset_data = []
        for user_asset in user_assets:
            if user_asset["user_id"] == user_id:
                asset_id = user_asset["asset_id"]
                quantity = user_asset["quantity"]
                asset_symbol = next(asset["symbol"] for asset in assets if asset["id"] == asset_id)
                user_asset_data.append({"asset_symbol": asset_symbol, "quantity": quantity})
        
        combined_data.append({"user_id": user_id, "username": user_name, "assets": user_asset_data})

    return combined_data

async def get_top_users_with_ethereum():
    pool = await get_pool()
    query = """
        SELECT
            u.id,
            u.username,
            SUM(ua.quantity) AS total_ethereum_quantity
        FROM
            users u
        JOIN
            user_assets ua ON u.id = ua.user_id
        JOIN
            assets a ON ua.asset_id = a.id
        WHERE
            a.symbol = 'ETH'
        GROUP BY
            u.id, u.username
        ORDER BY
            total_ethereum_quantity DESC
        LIMIT
            2;
    """
    pool = await get_pool()
    result = await fetch_data(pool, query)
    return result

@router.get("/top_ethereum_users", tags=["services"])
async def top_ethereum_users():
    print("getting users....")
    response = requests.get("http://localhost:8000/users")
    return response.json()
    #return await get_top_users_with_ethereum()