from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from . import app

engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime, UniqueConstraint

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(21), unique=True)
    email = (Column(String(254), unique=True))
    password = (Column(String(100)))
    created_datetime = Column(DateTime, default=datetime.datetime.now)
    updated_datetime = Column(DateTime, default=datetime.datetime.now)
    ig_oauth_token = (Column(String(100)))
    ig_username = (Column(String(100)))
    ig_fullname = (Column(String(100)))
    ig_profile_pic = (Column(String(100)))
    ig_datetime = Column(DateTime, default=datetime.datetime.now)

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key = True)
    category = Column(String(40))
    user_id = (Column(Integer(40)))
    media = (Column(String(2000)))
    hero_image = (Column(String(100)))

Base.metadata.create_all(engine)