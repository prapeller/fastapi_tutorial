import uvicorn
from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles

from database.database import Base
from database.database import engine
from dependencies import get_token_header
from routers.admin import router as admin_router
from routers.index import router as index_router
from routers.items import router as items_router
from routers.users import router as users_router

Base.metadata.create_all(bind=engine)

app = FastAPI(dependencies=[Depends(get_token_header)])
app.mount('/static', StaticFiles(directory='static'), name='static')

app.include_router(index_router)
app.include_router(users_router, prefix='/users', tags=['users'])
app.include_router(items_router, prefix='/items', tags=['items'])
app.include_router(admin_router, prefix="/admin", tags=["admin"],
                   responses={418: {"description": "I'm a teapot"}})

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=5006)
