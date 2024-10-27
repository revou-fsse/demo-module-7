from connectors.db import Base
from flask_login import UserMixin
from sqlalchemy import Column, Enum, Integer, String
from bcrypt import hashpw, gensalt, checkpw

class User(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    role = Column(Enum('admin', 'user'), nullable=False, default='user')

    def set_password(self, password):
        self.password = hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')
    
    def check_password(self, password):
        return checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"
