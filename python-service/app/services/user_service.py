from typing import Annotated

from fastapi import Depends

from app.data.repositories.user_repository import UserRepository
from app.services.base_service import BaseService
from app.data.domains.user import User

class UserService(BaseService[User]):
    def __init__(self, user_repository: Annotated[UserRepository, Depends(UserRepository)]):
        super().__init__(user_repository)
        self.user_repository = user_repository

    async def get_user_by_email(self, email: str) -> User:
        return await self.user_repository.get_user_by_email(email)