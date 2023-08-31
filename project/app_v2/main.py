from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from project.app_v2.routers import users, assets, user_assets, services
from project.app_v2.database.database import create_pg_pool

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8080",
    "http://localhost:3000",
    "127.0.0.1:59691"
]
# Apply CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(users.router)
app.include_router(assets.router)
app.include_router(user_assets.router)
app.include_router(services.router)

@app.on_event("startup")
async def startup_event():
    global pool
    app.pool = await create_pg_pool()

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

