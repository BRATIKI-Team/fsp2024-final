from motor.motor_asyncio import AsyncIOMotorDatabase

def get_db() -> AsyncIOMotorDatabase:
    from motor.motor_asyncio import AsyncIOMotorClient
    from app.core.config import DATABASE_CONNECTION_STRING, DATABASE_NAME

    client = AsyncIOMotorClient(DATABASE_CONNECTION_STRING)
    return client.get_database(DATABASE_NAME)