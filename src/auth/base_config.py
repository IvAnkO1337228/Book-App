from fastapi_users.authentication import (JWTStrategy,
                                           AuthenticationBackend, CookieTransport)
from fastapi_users import FastAPIUsers
from config import SECRET_AUTH
from auth.models import User
from auth.manager import get_user_manager


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET_AUTH, lifetime_seconds=3600)



auth_backend = AuthenticationBackend(
    name="jwt",
    transport=CookieTransport(cookie_name="bonds", cookie_max_age=3600),
    get_strategy=get_jwt_strategy,
)



fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()