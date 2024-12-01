from typing import Annotated, List, Optional

from fastapi import APIRouter, Depends, Body

from app.api.dto.login_dto import LoginDto
from app.api.dto.login_result_dto import LoginResultDto
from app.api.dto.refresh_token_request_dto import RefreshTokenReq
from app.api.dto.register_dto import RegisterDto
from app.data.domains.user import User
from app.services.auth_service import AuthService
from app.services.user_service import UserService

router = APIRouter()

@router.post("/register", name="users:register")
async def register(
        register_dto: Annotated[RegisterDto, Body(...)],
        auth_service: Annotated[AuthService, Depends(AuthService)]
) -> bool:
    return await auth_service.register(register_dto)

@router.post("/login", name="users:login")
async def login(
        login_dto: Annotated[LoginDto, Body(...)],
        auth_service: Annotated[AuthService, Depends(AuthService)]
) -> LoginResultDto:
    return await auth_service.login(login_dto)

@router.post("/refresh-token", name="users:refresh-token")
async def refresh_token(
        refresh_token_req: Annotated[RefreshTokenReq, Body(...)],
        auth_service: Annotated[AuthService, Depends(AuthService)]
) -> LoginResultDto:
    return await auth_service.refresh_token(refresh_token_req)

# to require jwt inject require_user method from AuthService
@router.get("/get-all", name="users:get-all")
async def get_all(
        user_id: Annotated[str, Depends(AuthService.require_user_id)],
        user_service: Annotated[UserService, Depends(UserService)]
) -> List[User]:
    return await user_service.get_all()

@router.get("/{user_id}", name="users:get-by-id")
async def get_by_id(
        user_id: str,
        user_service: Annotated[UserService, Depends(UserService)]
) -> Optional[User]:
    return await user_service.get(user_id)

@router.delete("/{user_id}", name="users:delete-by-id")
async def delete_by_id(
        user_id: str,
        user_service: Annotated[UserService, Depends(UserService)]
) -> bool:
    return await user_service.delete(user_id)