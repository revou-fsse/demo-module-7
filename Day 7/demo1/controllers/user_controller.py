from flask import Blueprint, request, redirect, url_for
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from connectors.db import connection
from models.user_model import User
from flask_login import login_user

userBp = Blueprint('user', __name__)

@userBp.route('/user/test')
def userTest():
    Session = sessionmaker(connection)
    with Session() as session:
        session.execute(text('INSERT INTO users (name, email, password) VALUES ("test", "test", "test")'))
        session.commit()
        return 'OK'


@userBp.route('/user')
def user():
    return 'user'

@userBp.route('/user/login', methods=['POST'])
def user_login():
    email = request.form.get('email')
    password = request.form.get('password')
    Session = sessionmaker(connection)

    with Session() as session:
        user = session.query(User).filter(User.email == email).first()

        if user.check_password(password):
            login_user(user)
            return redirect(url_for('home', name=user.name))
        else:
            return 'Invalid email or password'

@userBp.route('/user/register', methods=['POST'])
def user_register():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    print(name, email, password)
    Session = sessionmaker(connection)
    
    with Session() as session:
        try:
            user = User(name=name, email=email)
            user.set_password(password)
            print(user)
            session.add(user)
            session.commit()
            login_user(user)
            print(user)
            return redirect(url_for('home', name=user.name))
        except Exception as e:
            print(e)
            session.rollback()
            return 'Error registering user'