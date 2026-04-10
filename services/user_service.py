from models.user import User, UserInDb, UserToCreate
from protocols import PUserRepository
from errors.business_errors import UserNotFoundError, UserEmailAlreadyExistsError, UserPhoneAlreadyExistsError

class UserService:
    __user_repository: PUserRepository

    def __init__(self, user_repository: PUserRepository):
        self.__user_repository = user_repository

    def __get_user_or_raise(self, user_id: int) -> UserInDb:
        user = self.__user_repository.get_user_by_id(user_id)

        if not user:
            raise UserNotFoundError(user_id)

        return user

    def __ensure_email_is_available(self, email: str) -> None:
        user = self.__user_repository.get_user_by_email(email)

        if user:
            raise UserEmailAlreadyExistsError(email)

    def __ensure_phone_is_available(self, phone: str) -> None:
        user = self.__user_repository.get_user_by_phone(phone)

        if user:
            raise UserPhoneAlreadyExistsError(phone)

    def get_user_by_id(self, user_id: int) -> User:
        return User(**self.__get_user_or_raise(user_id).model_dump())

    def create_user(self, user_data: UserToCreate) -> User:
        self.__ensure_email_is_available(user_data.email)
        self.__ensure_phone_is_available(user_data.phone)
        return User(**self.__user_repository.create_user(user_data).model_dump())

    def update_user(self, user_id: int, user_data: UserToCreate) -> User:
        user = self.__get_user_or_raise(user_id)

        if user.email != user_data.email:
            self.__ensure_email_is_available(user_data.email)
        if user.phone != user_data.phone:
            self.__ensure_phone_is_available(user_data.phone)

        return User(**self.__user_repository.update_user(user_id, user_data).model_dump())

    def delete_user(self, user_id: int) -> None:
        self.__get_user_or_raise(user_id)
        self.__user_repository.delete_user(user_id)