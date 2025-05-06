from fastapi import APIRouter


router = APIRouter(prefix="/api/v1/posts", tags=["Posts"],responses={404: {"description": "Not found"}})


@router.post("/login")
async def login():
    return {"message": "Login endpoint"}
