from motor.motor_asyncio import AsyncIOMotorClient

MONGODB_URL = "mongodb://root:example@mongo:27017?retryWrites=true&w=majority"
client = AsyncIOMotorClient(MONGODB_URL)
