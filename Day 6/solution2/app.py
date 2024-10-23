from flask import Flask, render_template, request
from connectors.db import engine, Base, connection
from sqlalchemy import select, text, update, or_
from sqlalchemy.orm import sessionmaker
from models.product_model import Product
from models.product_review_model import ProductReview

Base.metadata.create_all(engine, checkfirst=True)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', nama='Asep', umur=11)

@app.route('/product')
def product():
    Session = sessionmaker(connection)
    with Session() as session:
        products = session.execute(text('select p.product_id, p.name, p.price, p.description, r.review_content from products p join product_reviews r on r.product_id = p.product_id')).all()

        return render_template('index.html', products=products, nama='Udin')

@app.route('/search')
def search():
    search_query = request.args.get('search_query')
    print(search_query)
    Session = sessionmaker(connection)
    with Session() as session:
        products = session.execute(text(f'select p.product_id, p.name, p.price, p.description, r.review_content from products p join product_reviews r on r.product_id = p.product_id where p.name like \'%{search_query}%\' or p.description like \'%{search_query}%\' or r.review_content like \'%{search_query}%\'')).all()
        return render_template('index.html', products=products, nama='Udin')


@app.route('/masukin_data')
def masukin_data():
    Session = sessionmaker(connection)
    with Session() as session:
        try:
            # insert menggunakan SQL
            session.execute(text('INSERT INTO products (name, price, description) VALUES (:name, :price, :description)'), [
                {
                    'name': 'T-Shirt',
                    'price': 50000,
                    'description': 'Hilfiger'
                },
                {
                    'name': 'Jeans',
                    'price': 100000,
                    'description': 'Levis'
                },
                {
                    'name': 'GT Man',
                    'price': 33000,
                    'description': 'Cel dalam'
                }
            ])
            products = session.execute(text('SELECT product_id, name FROM products')).all()

            # insert menggunakan ORM
            for product in products:
                session.add(ProductReview(product_id=product.product_id, email='standar@example.com', review_content=f'review product {product.name}', rating=4))

            session.commit()
            return 'success'
        except Exception as e:
            print(e)
            session.rollback()
            return 'failed'

@app.route('/update_data')
def update_data():
    Session = sessionmaker(connection)
    with Session() as session:
        session.execute(update(Product).where(Product.name == 'Jeans').values(price=120000))
        session.commit()
        return 'success'

@app.route('/delete_data')
def delete_data():
    Session = sessionmaker(connection)
    with Session() as session:
        try:
            session.execute(text('DELETE FROM products'))
            session.commit()
            return 'success'
        except Exception as e:
            print(e)
            session.rollback()
            return 'failed'