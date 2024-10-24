from connectors.db import Base
from sqlalchemy import Column, Integer, String
from flask_login import UserMixin
from bcrypt import hashpw, gensalt, checkpw

class User(Base, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)

    def __repr__(self):
        return f'<User {self.name} {self.email} {self.password}>'
    
    def set_password(self, password):
        self.password = hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')

    def check_password(self, password):
        return checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

