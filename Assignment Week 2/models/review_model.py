from connectors.db import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    description = Column(String(255), nullable=False)
    rating = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Review(id={self.id}, user_id={self.user_id}, description={self.description}, rating={self.rating})>"
