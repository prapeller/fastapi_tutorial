from pydantic import BaseModel


class ItemSchemaBase(BaseModel):
    title: str
    description: str | None = None


class UserSchemaBase(BaseModel):
    email: str


class ItemSchemaCreate(ItemSchemaBase):
    pass


class ItemSchemaRead(ItemSchemaBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserSchemaCreate(UserSchemaBase):
    password: str


class UserSchemaRead(UserSchemaBase):
    id: int
    is_active: bool
    items: list[ItemSchemaRead] = []

    class Config:
        orm_mode = True
