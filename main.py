from fastapi import FastAPI
from routers.user_router import router as user_router
from routers.auth_router import router as auth_router
from middlewares.error_handler import exception_handler

app = FastAPI()

app.add_exception_handler(Exception, exception_handler)

app.include_router(user_router)
app.include_router(auth_router)