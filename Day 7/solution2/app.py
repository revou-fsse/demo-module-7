from flask import Flask, jsonify
from connectors.db import Base, engine
from controllers.user_controller import userBp
from flask_jwt_extended import JWTManager
import os

Base.metadata.create_all(engine)

app = Flask(__name__)

jwt = JWTManager(app)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

app.register_blueprint(userBp)

@app.route('/')
def home():
    return jsonify({
        'status': 'LIVE'
    })