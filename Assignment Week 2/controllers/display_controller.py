from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_required, current_user
from flask_jwt_extended import jwt_required
from sqlalchemy import text
from models.user_model import User
from models.review_model import Review
from connectors.db import Session
from services.user_service import role_required

displayBp = Blueprint('display', __name__)

@displayBp.route('/')
def index():
    return render_template('index.html', current_user=current_user)

@displayBp.route('/login', methods=['GET'])
def login():
    error = request.args.get('error')
    return render_template('login.html', error=error, current_user=current_user)

@displayBp.route('/register', methods=['GET'])
def register():
    error = request.args.get('error')
    return render_template('register.html', error=error, current_user=current_user)

@displayBp.route('/unauthorized', methods=['GET'])
def unauthorized():
    return render_template('unauthorized.html', current_user=current_user)

@displayBp.route('/home', methods=['GET'])
@login_required
def home():
    try:
        with Session() as session:
            reviews = session.query(Review.description, Review.rating, User.name).join(User, User.id == Review.user_id).all()
            print(reviews)
            return render_template('home.html', current_user=current_user, reviews=reviews)
    except Exception as e:
        print(e)
        return redirect(url_for('display.index', current_user=current_user))

@displayBp.route('/review', methods=['GET'])
@login_required
@role_required('admin')
def review():
    try:
        with Session() as session:
            reviews = session.query(Review).all()
            return render_template('review.html', reviews=reviews, current_user=current_user)
    except Exception as e:
        print(e)
        return redirect(url_for('display.index', current_user=current_user))
    
@displayBp.route('/review/create', methods=['GET'])
@login_required
@role_required('admin')
def create_review():
    error = request.args.get('error')
    return render_template('create_review.html', error=error, current_user=current_user)

@displayBp.route('/review/update', methods=['GET'])
@login_required
@role_required('admin')
def update_review():
    error = request.args.get('error')
    review_id = request.args.get('review_id')

    try:
        with Session() as session:
            review = session.query(Review).get(review_id)
            return render_template('update_review.html', review=review, error=error, current_user=current_user)
    except Exception as e:
        print(e)
        return render_template('update_review.html', review=[], error=error, current_user=current_user)