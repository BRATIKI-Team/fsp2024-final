from pydantic import BaseModel


class LoginResultDto(BaseModel):
    id: str
    email: str
    token: str
    refresh_token: str