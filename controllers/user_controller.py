from fastapi import HTTPException
from models.user import User, UserToCreate
from errors.business_errors import (
    UserNotFoundError,
    UserEmailAlreadyExistsError,
    UserPhoneAlreadyExistsError,
)
from services.user_service import UserService


class UserController:
    __user_service: UserService

    def __init__(self, user_service: UserService):
        self.__user_service = user_service

    def get_me(self, user_id: int) -> User:
        try:
            return self.__user_service.get_user_by_id(user_id)
        except UserNotFoundError as exception:
            raise HTTPException(status_code=exception.status_code, detail=exception.message)

    def update_me(self, user_id: int, user_data: UserToCreate) -> User:
        try:
            return self.__user_service.update_user(user_id, user_data)
        except (UserNotFoundError, UserEmailAlreadyExistsError, UserPhoneAlreadyExistsError) as exception:
            raise HTTPException(status_code=exception.status_code, detail=exception.message)

    def delete_me(self, user_id: int) -> None:
        try:
            self.__user_service.delete_user(user_id)
        except UserNotFoundError as exception:
            raise HTTPException(status_code=exception.status_code, detail=exception.message)
