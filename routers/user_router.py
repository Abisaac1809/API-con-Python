from fastapi import APIRouter, Depends
from models.user import User, UserToCreate
from controllers.user_controller import UserController
from services.user_service import UserService
from repositories import UserRepository
from middlewares.auth_middleware import get_current_user_id

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


def get_controller() -> UserController:
    return UserController(UserService(UserRepository()))


@router.get("/me", response_model=User)
def get_user(
    user_id: int = Depends(get_current_user_id),
):
    return get_controller().get_me(user_id)


@router.put("/me", response_model=User)
def update_user(
    user_data: UserToCreate,
    user_id: int = Depends(get_current_user_id),
):
    return get_controller().update_me(user_id, user_data)


@router.delete("/me", status_code=204)
def delete_user(
    user_id: int = Depends(get_current_user_id),
):
    get_controller().delete_me(user_id)
