from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///restaurants.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


from lib.models.restaurant import Restaurant
from lib.models.review import Review
from lib.models.menu import MenuItem 

def create_tables():
    Base.metadata.create_all(engine)

def drop_tables():
    Base.metadata.drop_all(engine)