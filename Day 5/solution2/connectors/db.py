from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
import os
from models.product_model import Base

print('Connecting to database')
engine = create_engine(f'mysql+mysqlconnector://{os.getenv("DB_USERNAME")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}')

connection = engine.connect()
print('Connected to database')

Base.metadata.create_all(engine, checkfirst=True)

Session = sessionmaker(connection)