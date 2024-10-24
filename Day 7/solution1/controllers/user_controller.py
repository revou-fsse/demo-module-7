from flask import Blueprint, flash, request, render_template, redirect, url_for
from models.user_model import UserModel
from connectors.db import Session
from flask_login import login_user, logout_user

userBp = Blueprint('userBp', __name__)


@userBp.route('/user/login', methods=['POST'])
def user_login():
    email = request.form.get('email')
    password = request.form.get('password')

    with Session() as session:
        try:
            user = session.query(UserModel).filter(UserModel.email == email).first()
            if user and user.check_password(password):
                login_user(user)
                return redirect(url_for('home', name=user.name))
            else:
                return redirect(url_for('login', error='Wrong email or password'))
        except Exception as e:
            print(e)
            return redirect(url_for('login', error='Something wrong happened'))


@userBp.route('/user/register', methods=['POST'])
def user_register():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    with Session() as session:
        try:
            user = UserModel(name=name, email=email)
            user.set_password(password)
            session.add(user)
            session.commit()
            login_user(user)
            return redirect(url_for('home', name=name))
        except Exception as e:
            print(e)
            return redirect(url_for('register', error='Something wrong happened'))

@userBp.route('/logout')
def user_logout():
    logout_user()
    return redirect(url_for('index'))
    