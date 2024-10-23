from flask import Flask, jsonify
from sqlalchemy import select, text
from sqlalchemy.orm import sessionmaker
from connectors.db import connection, engine
from connectors.base import Base
from models.product import Product
from models.product_review import ProductReview
app = Flask(__name__)

Base.metadata.create_all(engine, checkfirst=True)

@app.route('/')
def home():    
    return "<p>Hello, World!</p>"
    
# get all products
@app.route('/product')
def product():
    Session = sessionmaker(connection)
    with Session() as session:
        products = session.execute(text('SELECT * FROM products'))
        return jsonify([{ "name": product.name } for product in products])
    
# insert product
@app.route('/product/insert')
def productInsert():
    Session = sessionmaker(connection)
    with Session() as session:
        try:
            session.execute(text('INSERT INTO products (name, price, description) VALUES (:name, :price, :description)'), 
            [
                {
                    'name': 'test',
                    'price': 100,
                    'description': 'test'
                }
            ]
            )
            session.commit()
            return {'status': 'success'}
        except:
            return {'status': 'error'}
        
# get all product reviews
@app.route('/product_reviews')
def productReviews():
    Session = sessionmaker(connection)
    with Session() as session:
        products = session.execute(select(ProductReview)).scalars().all()
        return jsonify([{ "name": product.name } for product in products])
    
# insert product reviews
@app.route('/product_reviews/insert')
def productReviewsInsert():
    Session = sessionmaker(connection)
    with Session() as session:
        try:
            product = session.execute(text('SELECT product_id FROM products')).first()

            session.execute(text('INSERT INTO product_reviews (product_id, email, name, review) VALUES (:product_id, :email, :name, :review)'), 
            [
                {
                    'product_id': product.product_id,
                    'email': 'test',
                    'name': 'test',
                    'review': 'test'
                }
            ]
            )
            session.commit()
            return {'status': 'success'}
        except:
            return {'status': 'error'}
        
# get join between products and product reviews
@app.route('/product_reviews/join')
def productReviewsJoin():
    Session = sessionmaker(connection)
    with Session() as session:
        products_reviews = session.execute(text('SELECT products.name as product_name, product_reviews.review as review FROM products INNER JOIN product_reviews ON products.product_id = product_reviews.product_id')).all()
        return jsonify([{ "name": product.product_name, "review": product.review } for product in products_reviews])