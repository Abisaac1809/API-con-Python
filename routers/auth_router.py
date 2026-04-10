from fastapi import APIRouter, Response
from models.user import User, UserToCreate
from models.auth import AuthResponse, LoginRequest
from controllers.auth_controller import AuthController
from services.auth_service import AuthService
from repositories import UserRepository

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

def get_user_repository() -> UserRepository:
    return UserRepository()

def get_controller() -> AuthController:
    auth_service = AuthService(get_user_repository())
    return AuthController(auth_service)


@router.post("/register", response_model=AuthResponse, status_code=201)
def register(response: Response, user_data: UserToCreate):
    return get_controller().register(response, user_data)


@router.post("/login", response_model=AuthResponse)
def login(response: Response, credentials: LoginRequest):
    return get_controller().login(response, credentials.email, credentials.password)
