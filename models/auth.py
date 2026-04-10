from pydantic import BaseModel, EmailStr
from .user import User

class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    user: User


class AuthResponse(BaseModel):
    message: str
    user: User
