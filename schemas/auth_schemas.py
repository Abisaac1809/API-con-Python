from pydantic import BaseModel, EmailStr
from schemas.user_schemas import UserResponse

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class AuthResponse(BaseModel):
    message: str
    user: UserResponse
