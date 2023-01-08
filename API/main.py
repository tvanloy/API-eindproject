import fastapi
import sqlalchemy.orm as orm
from fastapi import FastAPI
from typing import List
import os
import crud
import schemas

if not os.path.exists('./sqlitedb'):
    os.makedirs('./sqlitedb')

app = FastAPI()

crud.create_database()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: orm.Session = fastapi.Depends(crud.get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise fastapi.HTTPException(
            status_code=400, detail="woops email is in use"
        )
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0,
               limit: int = 10,
               db: orm.Session = fastapi.Depends(crud.get_db),
               ):
    users = crud.get_users(db=db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: orm.Session = fastapi.Depends(crud.get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise fastapi.HTTPException(status_code=404, detail="this user does not exist")
    return db_user


@app.post("/users/{user_id}/posts/", response_model=schemas.Quote)
def create_quote(user_id: int, quote: schemas.QuoteCreate, db: orm.Session = fastapi.Depends(crud.get_db)):
    return crud.create_quote(db=db, quote=quote, user_id=user_id)


@app.get("/quotes/", response_model=List[schemas.Quote])
def read_quotes(skip: int = 0, limit: int = 10, db: orm.Session = fastapi.Depends(crud.get_db)):
    quotes = crud.get_quotes(db=db, skip=skip, limit=limit)
    return quotes


@app.get("/quotes/{quote_id}", response_model=schemas.Quote)
def read_quote(quote_id: int, db: orm.Session = fastapi.Depends(crud.get_db)):
    quote = crud.get_quote(db=db, quote_id=quote_id)
    if quote is None:
        raise fastapi.HTTPException(status_code=404, detail='quote does not exist')

    return quote


@app.delete("/quotes/{quote_id}")
def delete_quote(quote_id: int, db: orm.Session = fastapi.Depends(crud.get_db)):
    crud.delete_quote(db=db, quote_id=quote_id)
    return {"message": f"deleted quote with id : {quote_id}"}


@app.put("/quotes/{post_id}", response_model=schemas.Quote)
def update_quote(quote_id: int, quote: schemas.QuoteCreate, db: orm.Session = fastapi.Depends(crud.get_db)):
    return crud.update_quote(db=db, quote=quote, quote_id=quote_id)
