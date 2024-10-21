import json
from flask import Blueprint, jsonify
from connectors.db import Session
from models.product_model import Product
from sqlalchemy import text, select

bp = Blueprint("product", __name__)

@bp.route("/product")
def product():
    with Session() as session:
        products_db = session.execute(select(Product)).scalars()
        products = [{"id": product.id, "name": product.name, "price": product.price, "description": product.description} for product in products_db]
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