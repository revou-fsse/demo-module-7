from sqlalchemy import create_engine
import os

print('Connecting to database...')

engine = create_engine(f'mysql+mysqlconnector://{os.getenv("DB_USERNAME")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}')

connection = engine.connect()

print('database connected')

