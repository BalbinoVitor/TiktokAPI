from fastapi import APIRouter


router = APIRouter(prefix="/api/v1/auth", tags=["Auth"],responses={404: {"description": "Not found"}})


@router.post("/login", summary="Login to the system",description="This endpoint allows users to log in to the system. It requires a username and password. If the credentials are valid, it returns a success message and a token for further authentication.")
async def login():
    return {"message": "Login endpoint"}
