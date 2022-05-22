from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.models import ItemModel
from database.schemas import ItemSchemaRead, ItemSchemaCreate
from dependencies import get_db, get_token_header

router = APIRouter(responses={404: {'description': 'item not found'}})


@router.get("/", response_model=list[ItemSchemaRead])
def items_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = db.query(ItemModel).offset(skip).limit(limit).all()
    return items


@router.get("/{id}", response_model=list[ItemSchemaRead])
def items_read(id: int, db: Session = Depends(get_db)):
    item = db.query(ItemModel).filter_by(id=id).first()
    if not item:
        raise HTTPException(status_code=404, detail='item not found')
    return item


@router.post("/{user_id}", response_model=ItemSchemaRead)
async def items_create(user_id: int, item_ser: ItemSchemaCreate, db: Session = Depends(get_db)):
    item = ItemModel(**item_ser.dict(), user_id=user_id)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@router.put("/{item_id}",
            tags=["custom"],
            responses={403: {"description": "Operation forbidden"}},
            )
async def items_update(item_id: str):
    if item_id != "plumbus":
        raise HTTPException(status_code=403, detail="You can only update the item: plumbus")
    return {"item_id": item_id, "name": "The great Plumbus"}
