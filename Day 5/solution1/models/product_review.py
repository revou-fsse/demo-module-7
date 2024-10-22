from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, func
from connectors.base import Base

class ProductReview(Base):
    __tablename__ = 'product_reviews'

    product_review_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.product_id'), nullable=False)
    email = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    review = Column(Text())
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'<ProductReview(product_review_id={self.product_review_id}, product_id={self.product_id}, email={self.email}, name={self.name})>'