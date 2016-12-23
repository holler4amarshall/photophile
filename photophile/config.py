import os
class DevelopmentConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://ubuntu:thinkful@localhost:5432/photophile"
    DEBUG = True
    
class InstagramConfig(object): 
    REDIRECT_URI = "localhost:5432/photophile/search"