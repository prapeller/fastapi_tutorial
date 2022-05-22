from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session

from database.models import UserModel
from database.schemas import UserSchemaRead, UserSchemaCreate
from dependencies import get_db, get_token_header
from services.notificator import write_notification

router = APIRouter(dependencies=[Depends(get_token_header)])


@router.get("/", response_model=list[UserSchemaRead])
def users_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(UserModel).offset(skip).limit(limit).all()
    return users


@router.get("/{user_id}", response_model=UserSchemaRead)
def users_read(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter_by(id=user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=UserSchemaRead)
def users_create(user_ser: UserSchemaCreate, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter_by(email=user_ser.email).first()
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    fake_hashed_password = user_ser.password + "notreallyhashed"
    user = UserModel(email=user_ser.email, hashed_password=fake_hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.post("send-notification-to/{user_id}")
async def users_send_notification(user_id: int, background_tasks: BackgroundTasks,
                                  db: Session = Depends(get_db)):
    user = db.query(UserModel).filter_by(id=user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    email = user.email
    for _ in range(10):
        background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"}
