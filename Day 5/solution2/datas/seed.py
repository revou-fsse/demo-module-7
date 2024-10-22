import json
from connectors.db import Session
from models.product_model import Product

# Load seed data from JSON file
with open('./datas/seed.json') as f:
    seed_data = json.load(f)

# Create a new database connection for seeding data
with Session() as session:
    # Seed data
    for data in seed_data:
        product = Product(name=data['name'], price=data['price'], description=data['description'])
        session.add(product)
        session.commit()