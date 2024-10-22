import json
from flask import Blueprint, jsonify
from connectors.db import Session
from models.product_model import Product
from sqlalchemy import text, select

bp = Blueprint("product", __name__)

@bp.route("/product")
def product():
    with Session() as session:
        # text('select name from products')
        # ORM select(Product)
        products_db = session.execute(text('select name from products')).all()
        print(products_db)
        products = [{"name": product.name} for product in products_db]
        return jsonify(products)
    
@bp.route('/product/seed')
def seed():
    with open('./datas/seed.json') as f:
        seed_data = json.load(f)
    with Session() as session:
        # Seed data
        for data in seed_data:
            product = Product(name=data['name'], price=data['price'], description=data['description'])
            session.add(product)
            session.commit()
        return 'seeded'

@bp.route('/products/delete')
def delete():
    with Session() as session:
        session.execute(text('DELETE FROM products'))
        session.commit()
        return 'deleted'