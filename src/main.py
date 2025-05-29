from fastapi import FastAPI
from contextlib import asynccontextmanager

from .core.db import init_db

from .features.user.user_router import router as user_router

# from .features.gpt.gpt_router import router as gpt_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup operations
    init_db()
    yield
    # Shutdown operations (if any)


app = FastAPI(lifespan=lifespan)


@app.get("/")
def get_root(token: str):
    return {"Message" "Welcome To BetterStart"}


# # Include the routers
app.include_router(user_router, prefix="/api/v1", tags=["users"])
# app.include_router(gpt_router, prefix="/api/v1", tags=["GPT"])
