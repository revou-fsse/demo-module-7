from flask import Flask, jsonify, redirect, url_for
from flask_login import LoginManager
from flask_jwt_extended import JWTManager, verify_jwt_in_request, get_jwt_identity
from models.user_model import User
from connectors.db import Base, engine, Session
from controllers.display_controller import displayBp
from controllers.user_controller import userBp
from controllers.review_controller import reviewBp

import os

Base.metadata.create_all(engine)

app = Flask(__name__)


app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

login_manager = LoginManager()
login_manager.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(displayBp)
app.register_blueprint(userBp)
app.register_blueprint(reviewBp)

@login_manager.user_loader
def load_user(user_id):
    try:
        with Session() as session:
            return session.query(User).get(user_id)
    except Exception as e:
        print(e)
        return None

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('display.unauthorized'))

@login_manager.request_loader
def load_user(request):
    try:
        verify_jwt_in_request()
        user = get_jwt_identity()
        with Session() as session:
            return session.query(User).get(user.id)
    except Exception as e:
        print(e)
        return None