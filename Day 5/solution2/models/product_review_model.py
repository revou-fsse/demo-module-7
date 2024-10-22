from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ProductReview(Base):
    __tablename__ = "product_reviews"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    email = Column(String(100))
    rating = Column(Integer)
    review_content = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<ProductReview(id={self.id}, product_id={self.product_id}, email={self.email}, rating={self.rating}, review_content={self.review_content}, created_at={self.created_at})>"