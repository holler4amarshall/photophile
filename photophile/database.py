from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from . import app

engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(1024))
    email = ()
    password = ()
    datetime = Column(DateTime, default=datetime.datetime.now)
    ig_oauth_token = ()
    ig_username = ()
    ig_fullname = ()
    ig_profile_pic = ()
    ig_datetime = Column(DateTime, default=datetime.datetime.now)

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key = True)
    category = ()
    user_id = ()
    media = ()
    hero_image = ()

Base.metadata.create_all(engine)