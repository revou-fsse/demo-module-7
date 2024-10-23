from connectors.db import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.sql import func

class ProductReview(Base):
    __tablename__ = 'product_reviews'
    product_review_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.product_id', ondelete='CASCADE'), nullable=False)
    rating = Column(Integer, nullable=False)
    review = Column(Text())
    email = Column(String(100), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<ProductReview(id={self.product_review_id}, product_id={self.product_id}, email={self.email}, rating={self.rating}, review_content={self.review}, created_at={self.created_at})>"