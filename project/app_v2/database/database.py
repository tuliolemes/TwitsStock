import asyncpg

pool = None

async def create_pg_pool():
    global pool
    pool = await asyncpg.create_pool(
        user="postgres",
        password="admin",
        database="Stocktwits",
        host="localhost",
    )


async def get_pool():
    if pool is None:
        await create_pg_pool()
    return pool
    
async def fetch_data(pool, query):
    async with pool.acquire() as connection:
        result = await connection.fetch(query)
    return result

