from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

print('connecting to db')
engine = create_engine('mysql+mysqlconnector://root:ramga9455159@localhost:3306/mas_owi')

connection = engine.connect()
print('connected to db')