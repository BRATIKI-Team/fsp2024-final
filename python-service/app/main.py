
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import user_router


def get_application() -> FastAPI:
    application = FastAPI(title="test_app")

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(user_router.router, tags=["users"], prefix="/user")

    return application

app = get_application()