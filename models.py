import sqlalchemy as sql
from database import Base
import sqlalchemy.orm as orm


class User(Base):
    __tablename__ = "users"

    id = sql.Column(sql.Integer, primary_key=True, index=True)
    email = sql.Column(sql.String, unique=True, index=True)
    hashed_password = sql.Column(sql.String)
    is_active = sql.Column(sql.Boolean, default=True)

    quotes = orm.relationship("Quote", back_populates='owner')


class Quote(Base):
    __tablename__ = "quotes"
    id = sql.Column(sql.Integer, primary_key=True, index=True)
    name = sql.Column(sql.String, index=True)
    quote = sql.Column(sql.String, index=True)
    owner_id = sql.Column(sql.Integer, sql.ForeignKey("users.id"))

    owner = orm.relationship("User", back_populates="quotes")
