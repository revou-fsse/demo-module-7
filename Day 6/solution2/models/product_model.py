from sqlalchemy import Column, Integer, String, DECIMAL, DateTime, func
from connectors.db import Base

class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(100), nullable=False)
    price = Column(DECIMAL(14, 2))
    description = Column(String(255))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<Product(product_id={self.product_id}, name={self.name}, price={self.price}, description={self.description}, created_at={self.created_at})"