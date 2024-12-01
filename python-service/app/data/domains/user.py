from typing import Optional

from pydantic import BaseModel

class User(BaseModel):
    id: Optional[str] = None
    email: str
    password: str

    class Config:
        from_attributes = True