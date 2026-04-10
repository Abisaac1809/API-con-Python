import jwt
from fastapi import HTTPException, Request
from services.auth_service import SECRET_KEY, ALGORITHM


def get_current_user_id(request: Request) -> int:
    token_cookie = request.cookies.get("access_token")
    if not token_cookie:
        raise HTTPException(status_code=401, detail="Authentication cookie missing")

    token = token_cookie
    if token_cookie.startswith("Bearer "):
        token = token_cookie.split(" ", 1)[1]

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return int(payload["sub"])
    except (jwt.InvalidTokenError, KeyError, ValueError):
        raise HTTPException(status_code=401, detail="Invalid or expired token")
