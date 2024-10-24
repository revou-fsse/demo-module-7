from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_required
from models.user_model import UserModel
from connectors.db import Session, Base, engine
from controllers.user_controller import userBp
import os

Base.metadata.create_all(engine)

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

login_manager = LoginManager()
login_manager.init_app(app)

app.register_blueprint(userBp)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/unauthorized')
def unauthorized():
    return render_template('unauthorized.html')

@app.route('/login')
def login():
    error = request.args.get('error')
    return render_template('login.html', error = error)

@app.route('/register')
def register():
    error = request.args.get('error')
    return render_template('register.html', error = error)

@app.route('/home')
@login_required
def home():
    name = request.args.get('name')
    return render_template('home.html', name=name)

@login_manager.user_loader
def load_user(user_id):
    try:
        with Session() as session:
            return session.query(UserModel).get(int(user_id))
    except Exception as e:
        print(e)
        return

@login_manager.unauthorized_handler
def handle_unauthorized():
    return redirect(url_for('unauthorized'))


