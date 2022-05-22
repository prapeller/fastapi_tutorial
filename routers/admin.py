from fastapi import APIRouter, Depends

from dependencies import get_token_query

router = APIRouter(dependencies=[Depends(get_token_query)])


@router.post("/")
async def update_admin():
    return {"message": "Admin getting schwifty"}
