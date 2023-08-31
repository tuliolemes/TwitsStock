from fastapi import FastAPI
import asyncpg


app = FastAPI()


async def create_pg_pool():
    return await asyncpg.create_pool(
        user="postgres",
        password="admin",
        database="Stocktwits",
        host="localhost",
    )

async def fetch_data(query):
    async with pool.acquire() as connection:
        result = await connection.fetch(query)
    return result

@app.on_event("startup")
async def startup_event():
    global pool
    pool = await create_pg_pool()

@app.get("/")
async def read_root():
    query = "SELECT * FROM assets"
    result = await fetch_data(query)
    return result

@app.get("/users")
async def read_root():
    query = "SELECT * FROM users"
    result = await fetch_data(query)
    return result

@app.get("/users/top/et")
async def retrieve_top_2_users():
    query = """SELECT u.username, u.email, ua.quantity
        FROM users u
        JOIN user_assets ua ON u.id = ua.user_id
        JOIN assets a ON ua.asset_id = a.id
        WHERE a.symbol = 'ETH'
        ORDER BY ua.quantity DESC
        LIMIT 2;"""
    result = await fetch_data(query)
    return result

@app.get("/top_ethereum_users")
async def get_top_ethereum_users():
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
    result = await fetch_data(query)
    return result

# @app.get("/")
# def calculate_mortgage(principal, interest, period):
#     period = float(period)
#     principal = float(principal)
#     n = period * 12
#     interest = int(interest) / (100 * 12)
#     interest = float(interest)
#     monthly_payment = principal*(interest*(1+interest)**n)/((1+interest)**n-1)

#     return monthly_payment