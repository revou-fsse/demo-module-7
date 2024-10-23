from flask import Flask, render_template, request
from sqlalchemy import select, text, update
from connectors.db import Base, engine, connection
from sqlalchemy.orm import sessionmaker
from controllers.product import productBp
from controllers.product_review import productReviewBp
from models.product import Product
from models.product_review import ProductReview

Base.metadata.create_all(engine, checkfirst=True)

app = Flask(__name__)

app.register_blueprint(productBp)
app.register_blueprint(productReviewBp)

@app.route("/")
def home():
    Session = sessionmaker(connection)
    with Session() as session:
        # products = session.execute(select(Product).where(Product.price > 100)).scalars().all()
        # products = session.execute(text('SELECT * FROM products JOIN product_reviews ON products.product_id = product_reviews.product_id')).all()
        products_reviews = session.query(Product, ProductReview).join(ProductReview, Product.product_id == ProductReview.product_id).all()

        print(products_reviews)
        return render_template('index.html', products=products_reviews)
    
@app.route('/search')
def search():
    # get from form
    product_name = request.args.get('product_name')
    print(product_name)
    Session = sessionmaker(connection)
    with Session() as session:
        products_reviews = session.query(Product, ProductReview).join(ProductReview, Product.product_id == ProductReview.product_id).filter(Product.name.like(f'%{product_name}%')).all()
        return render_template('index.html', products=products_reviews)
    
@app.route('/update')
def routeUpdate():
    Session = sessionmaker(connection)
    with Session() as session:
        # session.execute(text('UPDATE products SET name = :name WHERE product_id = :product_id'), [
        #     {
        #         'name': 'updated product again',
        #         'product_id': 31
        #     }
        # ])
        session.execute(update(Product).where(Product.product_id == 31).values(name='updated product'))
        session.commit()
        return 'updated'
    
@app.route('/seed', methods=['POST', 'GET'])
def seed():
    Session = sessionmaker(connection)
    with Session() as session:
        try:
            session.execute(text('INSERT INTO products (name, price, description) VALUES (:name, :price, :description)'), [
                {
                    'name': 'product1',
                    'price': 100,
                    'description': 'product description 1'
                },
                {
                    'name': 'product2',
                    'price': 200,
                    'description': 'product description 2'
                },
                {
                    'name': 'product3',
                    'price': 300,
                    'description': 'product description 3'
                },
            ])
            products = session.execute(select(Product)).scalars().all()
            for product in products:
                session.add(ProductReview(rating=5, email='review1', review=f'review product {product.name}', product_id=product.product_id))
            session.commit()
            return 'seeded'
        except Exception as e:
            print(e)
            session.rollback()
            return 'seed failed'
        
@app.route('/deleteSeed', methods=['DELETE', 'GET'])
def deleteSeed():
    Session = sessionmaker(connection)
    with Session() as session:
        try:
            session.begin()
            # session.execute(text('DELETE FROM product_reviews'))
            session.execute(text('DELETE FROM products'))
            session.commit()
            return 'deleted'
        except Exception as e:
            print(e)
            session.rollback()
            return 'failed'
        