from starlette.config import Config

config = Config(".env")

#DATABASE
DATABASE_CONNECTION_STRING = config("DATABASE_CONNECTION_STRING", cast=str)
DATABASE_NAME = config("DATABASE_NAME", cast=str)

print("CONNECTION STRING", DATABASE_CONNECTION_STRING)
print("DATBASE_NAME", DATABASE_NAME)

