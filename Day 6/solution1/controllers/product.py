from flask import Blueprint, render_template

productBp = Blueprint("product", __name__)

@productBp.route('/products')
def products():
    return 'hello products'
    
