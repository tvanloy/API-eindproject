from pydantic import BaseModel
import datetime as dt


class QuoteBase(BaseModel):
    name: str
    quote: str | None = None


class QuoteCreate(QuoteBase):
    pass


class Quote(QuoteBase):
    id: int
    owner_id: int


    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    quotes: list[Quote] = []

    class Config:
        orm_mode = True
