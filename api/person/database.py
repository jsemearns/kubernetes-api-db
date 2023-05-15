import os

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from .models import Person


async def init_db() -> None:
    # initialize collections
    client = AsyncIOMotorClient(f'mongodb://{os.environ.get("DB_URL")}:27017')
    if os.environ.get('DB_USE_AUTH'):
        client = AsyncIOMotorClient(f'mongodb://{os.environ.get("DB_USER_NAME")}:{os.environ.get("DB_PASSWORD")}@{os.environ.get("DB_URL")}:27017')
    mongo = client['person']
    await init_beanie(database=mongo, document_models=[Person])