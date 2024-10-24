from flask import Flask, render_template, request
from connectors.db import Session, connection, Base
from models.user_model import User
from controllers.user_controller import userBp
from flask_login import LoginManager, login_required
import os


Base.metadata.create_all(connection)

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

login_manager = LoginManager()
login_manager.init_app(app)

app.register_blueprint(userBp)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@login_manager.user_loader
def load_user(user_id):
    with Session() as session:
        user = session.query(User).get(user_id)
        return user
    
@app.route('/home')
@login_required
def home():
    name = request.args.get('name')
    return render_template('home.html', name=name)

@login_manager.unauthorized_handler
def unauthorized():
    return render_template('unauthorized.html')