from motor.motor_asyncio import AsyncIOMotorDatabase

from database import client


async def db_template() -> AsyncIOMotorDatabase:
    return client["form_template"]
