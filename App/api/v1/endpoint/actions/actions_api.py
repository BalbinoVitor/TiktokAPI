from fastapi import APIRouter


router = APIRouter(prefix="/api/v1/actions", tags=["Actions"],responses={404: {"description": "Not found"}})


@router.post("/login")
async def login():
    return {"message": "Login endpoint"}
