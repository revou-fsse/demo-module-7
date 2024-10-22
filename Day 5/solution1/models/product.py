from sqlalchemy import DECIMAL, Column, DateTime, Integer, String, Text, func
from connectors.base import Base

class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(100), nullable=False)
    price = Column(DECIMAL(14, 2))
    description = Column(Text())
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'<Product(product_id={self.product_id}, name={self.name})>'