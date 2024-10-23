from connectors.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DateTime, Text, func

class ProductReview(Base):
    __tablename__ = 'product_reviews'

    product_review_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    product_id = Column(Integer, ForeignKey('products.product_id', ondelete='CASCADE'), nullable=False)
    email = Column(String(100), nullable=False)
    review_content = Column(Text)
    rating = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
