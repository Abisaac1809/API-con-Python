from fastapi import Response
from schemas.auth_schemas import AuthResponse
from services.auth_service import AuthService


class AuthController:
    __auth_service: AuthService

    def __init__(self, auth_service: AuthService):
        self.__auth_service = auth_service

    def register(self, response: Response, user_data) -> AuthResponse:
        user = self.__auth_service.register(user_data)
        token = self.__auth_service.create_access_token(user)
        response.set_cookie(key="access_token", value=token, httponly=True, max_age=3600, expires=3600)
        return AuthResponse(message="Login Succesful", user=user)

    def login(self, response: Response, email: str, password: str) -> AuthResponse:
        user = self.__auth_service.login(email, password)
        token = self.__auth_service.create_access_token(user)
        response.set_cookie(key="access_token", value=token, httponly=True, max_age=3600, expires=3600)
        return AuthResponse(message="Login Succesful", user=user)
