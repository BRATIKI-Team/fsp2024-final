from typing import Annotated, List

from fastapi import APIRouter, Depends, Body

from app.api.dto.register_dto import RegisterDto
from app.data.domains.user import User
from app.services.user_service import UserService

router = APIRouter()

@router.post("/register", name="users:register")
async def register(
        register_dto: Annotated[RegisterDto, Body(...)],
        user_service: Annotated[UserService, Depends(UserService)]
) -> str:
    return await user_service.register(register_dto)

@router.get("/get-all", name="users:get-all")
async def get_all(
        user_service: Annotated[UserService, Depends(UserService)]
) -> List[User]:
    return await user_service.get_all()

@router.get("/{user_id}", name="users:get-by-id")
async def get_by_id(
        user_id: str,
        user_service: Annotated[UserService, Depends(UserService)]
) -> User:
    return await user_service.get(user_id)