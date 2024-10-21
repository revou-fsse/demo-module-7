from sqlalchemy import Column, Integer, String, Text, DECIMAL, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    price = Column(DECIMAL(10, 2))
    description = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}, price={self.price}, description={self.description})>"