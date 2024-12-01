from pydantic import BaseModel


class RegisterDto(BaseModel):
    email: str
    password: str