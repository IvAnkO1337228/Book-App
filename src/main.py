from fastapi import FastAPI, Depends
from auth.base_config import fastapi_users, auth_backend
from auth.schemas import UserRead, UserCreate

from auth.models import User
from auth.base_config import current_user
from pages.router import router as router_pages
from fastapi.staticfiles import StaticFiles

from operations.router import router as router_operations

app = FastAPI(
    title="Book App"
)


app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(router_pages)


app.include_router(router_operations)



# @app.get("/protected-route")
# def protected_route(user: User = Depends(current_user)):
#     return f"Hello, {user.username}"
