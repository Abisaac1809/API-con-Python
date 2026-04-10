from typing import Protocol
from models.user import UserToCreate, UserInDb

class PUserRepository(Protocol):
    def get_user_by_id(self, user_id: int) -> UserInDb | None:
        ...

    def get_user_by_email(self, email: str) -> UserInDb | None:
        ...

    def get_user_by_phone(self, phone: str) -> UserInDb | None:
        ...

    def get_list_of_users(self) -> list[UserInDb]:
        ...

    def create_user(self, user_data: UserToCreate) -> UserInDb:
        ...

    def update_user(self, user_id: int, user_data: UserToCreate) -> UserInDb:
        ...

    def delete_user(self, user_id: int) -> None:
        ...