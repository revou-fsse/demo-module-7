from connectors.db import Base
from sqlalchemy import Column, DateTime, Integer, String, func
from sqlalchemy.orm import relationship

class Product(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    price = Column(Integer)
    description = Column(String(100))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<Product(id={self.product_id}, name={self.name}, price={self.price}, description={self.description})>"
