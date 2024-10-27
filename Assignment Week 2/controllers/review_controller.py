from flask import Blueprint, request
from models.review_model import Review
from connectors.db import Session
from flask import redirect, url_for
from flask_login import current_user
from flask_jwt_extended import jwt_required
from services.user_service import role_required

reviewBp = Blueprint('review', __name__)

@reviewBp.route('/review', methods=['POST'])
@role_required('admin')
def add_review():
    description = request.form.get('description')
    rating = request.form.get('rating')

    if not description or not rating:
        return redirect(url_for('display.review', error='Please enter all fields'))

    try:
        with Session() as session:
            review = Review(description=description, rating=int(rating), user_id=current_user.id)
            session.add(review)
            session.commit()

            return redirect(url_for('display.review'))
    except Exception as e:
        print(e)
        return redirect(url_for('display.review', error='Something went wrong. Please try again.'))
    
@reviewBp.route('/review/update', methods=['POST'])
@role_required('admin')
def update_review():
    review_id = request.form.get('review_id')
    description = request.form.get('description')
    rating = request.form.get('rating')

    try:
        with Session() as session:
            review = session.query(Review).get(review_id)
            review.description = description
            review.rating = rating
            session.commit()

            return redirect(url_for('display.review'))
    except Exception as e:
        print(e)
        return redirect(url_for('display.review', error='Something went wrong. Please try again.'))
    
@reviewBp.route('/review/delete', methods=['POST'])
@role_required('admin')
def delete_review():
    review_id = request.form.get('review_id')

    try:
        with Session() as session:
            review = session.query(Review).get(review_id)
            session.delete(review)
            session.commit()

            return redirect(url_for('display.review'))
    except Exception as e:
        print(e)
        return redirect(url_for('display.review', error='Something went wrong. Please try again.'))