from fastapi import HTTPException, Response
from models.user import UserToCreate
from errors.business_errors import (
    InvalidCredentialsError,
    UserEmailAlreadyExistsError,
    UserPhoneAlreadyExistsError,
)
from services.auth_service import AuthService


class AuthController:
    __auth_service: AuthService

    def __init__(self, auth_service: AuthService):
        self.__auth_service = auth_service

    def register(self, response: Response, user_data: UserToCreate) -> dict:
        try:
            user = self.__auth_service.register(user_data)
            token = self.__auth_service.create_access_token(user)
            response.set_cookie(key="access_token",
                                value=token,
                                httponly=True,
                                max_age=3600,
                                expires=3600
                                )
            return {
                "message": "Login Succesful",
                "user": user
                }
        except (UserEmailAlreadyExistsError, UserPhoneAlreadyExistsError) as e:
            raise HTTPException(status_code=e.status_code, detail=e.message)

    def login(self, response: Response, email: str, password: str) -> dict:
        try:
            user = self.__auth_service.login(email, password)
            token = self.__auth_service.create_access_token(user)
            response.set_cookie(key="access_token",
                                value=token,
                                httponly=True,
                                max_age=3600,
                                expires=3600
                                )
            return {
                "message": "Login Succesful",
                "user": user
                }
        except InvalidCredentialsError as e:
            raise HTTPException(status_code=e.status_code, detail=e.message)
