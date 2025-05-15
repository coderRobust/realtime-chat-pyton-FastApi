from fastapi import Header, HTTPException


def get_current_user(authorization: str = Header(...)):
    if authorization == "Bearer mysecrettoken":
        return "User1"
    raise HTTPException(status_code=401, detail="Unauthorized")
