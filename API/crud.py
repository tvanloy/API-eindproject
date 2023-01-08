import database
import sqlalchemy.orm as orm
import schemas
import models


def create_database():
    return database.Base.metadata.create_all(bind=database.engine)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user_by_email(db: orm.Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: orm.Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notsecure"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: orm.Session, skip: int, limit: int):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user(db: orm.Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_quote(db: orm.Session, quote: schemas.QuoteCreate, user_id: int):
    quote = models.Quote(**quote.dict(), owner_id=user_id)
    db.add(quote)
    db.commit()
    db.refresh(quote)
    return quote


def get_quotes(db: orm.Session, skip: int, limit: int):
    return db.query(models.Quote).offset(skip).limit(limit).all()


def get_quote(db: orm.Session, quote_id: int):
    return db.query(models.Quote).filter(models.Quote.id == quote_id).first()


def delete_quote(db: orm.Session, quote_id: int):
    db.query(models.Quote).filter(models.Quote.id == quote_id).delete()
    db.commit()


def update_quote(db: orm.Session, quote_id: int, quote: schemas.QuoteCreate):
    db_quote = get_quote(db=db, quote_id=quote_id)
    db_quote.name = quote.name
    db_quote.quote = quote.quote
    db.commit()
    db.refresh(db_quote)
    return db_quote
