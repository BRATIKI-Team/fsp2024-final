from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")

#DATABASE
DATABASE_CONNECTION_STRING = config("DATABASE_CONNECTION_STRING", cast=str)
DATABASE_NAME = config("DATABASE_NAME", cast=str)

#JWT
JWT_SECRET_KEY = config("JWT_SECRET_KEY", cast=str)
JWT_ALGORITHM = config("JWT_ALGORITHM", cast=str)
ACCESS_TOKEN_EXPIRE_MINUTES = config("ACCESS_TOKEN_EXPIRE_MINUTES", cast=int)
