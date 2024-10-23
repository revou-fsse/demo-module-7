from flask import Blueprint

productReviewBp = Blueprint("product_review", __name__)

@productReviewBp.route('/product_reviews')
def products():
    return 'hello product review'
    
