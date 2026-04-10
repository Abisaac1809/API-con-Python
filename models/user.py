from datetime import datetime
from pydantic import BaseModel, EmailStr, Field

class BaseUser(BaseModel):
    name: str = Field(
        title='Full Name',
        min_length=3,
        max_length=100
    )

    email: EmailStr

    phone: str = Field(
        title='Phone Number',
        pattern=r'^\+[0-9]{2} [0-9]{3}-[0-9]{7}$',
        examples=['+57 300-1234567']
    )

class UserToCreate(BaseUser):
    password: str = Field(
        title='Password',
        min_length=6,
        max_length=30
    )

class User(BaseUser):
    id: int = Field(
        title='User ID'
    )

    created_at: datetime = Field(
        title='Creation Date',
        default_factory=datetime.now
    )

    updated_at: datetime = Field(
        title='Last Update Date',
        default_factory=datetime.now
    )

class UserInDb(User):
    password: str = Field(
        title='Password Hash'
    )


