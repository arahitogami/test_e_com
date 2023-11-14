from motor.motor_asyncio import AsyncIOMotorClient
import os

USER_ROOT = os.environ.get("MONGO_INITDB_ROOT_USERNAME", default="root")
USER_PASSWORD = os.environ.get("MONGO_INITDB_ROOT_PASSWORD", default="example")
MONGO_HOST = os.environ.get("MONGO_HOST", default="localhost")
MONGO_PORT = os.environ.get("MONGO_PORT", default="27017")

MONGODB_URL = (f"mongodb://{USER_ROOT}:{USER_PASSWORD}@"
               f"{MONGO_HOST}:{MONGO_PORT}?retryWrites=true&w=majority")

client = AsyncIOMotorClient(MONGODB_URL)
