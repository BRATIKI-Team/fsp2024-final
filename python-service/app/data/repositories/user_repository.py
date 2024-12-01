from typing import Annotated, Dict, Optional
from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.data.domains.user import User
from app.data.repositories.base_repository import BaseRepository, T
from app.core.dependecies import get_db


class UserRepository(BaseRepository):
    def __init__(self, db: Annotated[AsyncIOMotorDatabase, Depends(get_db)]):
        super().__init__(db, "users", User)

    async def get_user_by_email(self, email: str) -> Optional[User]:
        document = await self.collection.find_one({"email": email})
        return self._document_to_model(document) if document else None

    def serialize(self, document: Dict) -> T:
        return User(**document)

