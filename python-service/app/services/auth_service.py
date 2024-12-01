from datetime import timedelta, datetime, timezone
from http.client import HTTPException
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from app.api.dto.login_dto import LoginDto
from app.api.dto.login_result_dto import LoginResultDto
from app.api.dto.register_dto import RegisterDto
from app.core.config import JWT_SECRET_KEY, JWT_ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from app.data.domains.user import User
from app.services.user_service import UserService


class AuthService:
    def __init__(
            self,
            user_service: Annotated[UserService, Depends(UserService)]
    ):
        self.user_service = user_service
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    async def register(self, register_dto: RegisterDto) -> bool:
        user = await self.user_service.get_user_by_email(register_dto.email)
        if user is not None:
            raise ValueError("User with this email already exists")

        hashed_pwd = self.pwd_context.hash(register_dto.password)
        new_user = User(email=register_dto.email, password=hashed_pwd)
        user_id = await self.user_service.create(new_user)
        return user_id is not None

    async def login(self, login_dto: LoginDto) -> LoginResultDto:
        user = await self.user_service.get_user_by_email(login_dto.email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        creds = {"id": user.id, "sub": user.email}
        access_token = self.create_access_token(creds, access_token_expires)
        return LoginResultDto(id=user.id, email=user.email, token=access_token)

    @classmethod
    def create_access_token(cls, data: dict, expires_delta: timedelta) -> str:
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + expires_delta
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, key=JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
        return encoded_jwt

    @classmethod
    def get_current_user_id(
            cls,
            token: Annotated[str, Depends(OAuth2PasswordBearer(tokenUrl="token"))]
    ) -> User:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=JWT_ALGORITHM)
        user_id = payload.get("id")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )

        return user_id










