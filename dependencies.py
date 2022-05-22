from fastapi import Header, HTTPException

from database.database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_token_header(x_token: str = Header()):
    if x_token != "keycloak":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_token_query(token: str):
    if token != "jessica":
        raise HTTPException(status_code=400, detail="No Jessica token provided")
