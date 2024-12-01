from typing import Annotated

from bson import ObjectId
from fastapi import Depends

from app.api.dto.register_dto import RegisterDto
from app.data.repositories.user_repository import UserRepository
from app.services.base_service import BaseService
from app.data.domains.user import User

class UserService(BaseService):
    def __init__(self, user_repository: Annotated[UserRepository, Depends(UserRepository)]):
        super().__init__(user_repository)
        self.user_repository = user_repository

    async def register(self, register_dto: RegisterDto) -> str:
        user = User(email=register_dto.email, password=register_dto.password)
        return await self.user_repository.insert(user)


