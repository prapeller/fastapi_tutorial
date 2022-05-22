from fastapi import APIRouter, Depends

from dependencies import get_token_header

router = APIRouter(dependencies=[Depends(get_token_header)])


@router.get("/")
async def root():
    return {'message': 'hello root page'}
