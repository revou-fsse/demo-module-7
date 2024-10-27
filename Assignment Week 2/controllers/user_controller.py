from flask import Blueprint, redirect, request, url_for, jsonify
from connectors.db import Session
from models.user_model import User
from flask_login import login_user, logout_user, login_required
from flask_jwt_extended import create_access_token, unset_jwt_cookies, jwt_required

userBp = Blueprint('user', __name__)


@userBp.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    role = request.form.get('role')

    if not name or not email or not password or not role:
        return redirect(url_for('display.register', error='Please enter all fields'))

    try:
        with Session() as session:
            user = User(name=name, email=email, role=role)
            user.set_password(password)

            session.add(user)
            session.commit()

            login_user(user)
            create_access_token(identity={'id': user.id, 'name': user.name, 'email': user.email, 'role': user.role})

            return jsonify({'redirect': url_for('display.home')}), 200
    except Exception as e:
        print(e)
        return redirect(url_for('display.register', error='Something went wrong. Please try again.'))
    
@userBp.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        return redirect(url_for('display.login', error='Please enter both email and password'))

    try:
        with Session() as session:
            user = session.query(User).filter(User.email == email).first()
            isCorrectUser = user and user.check_password(password)

            if isCorrectUser:
                login_user(user)
                create_access_token(identity={'id': user.id, 'name': user.name, 'email': user.email, 'role': user.role})
                return jsonify({'redirect': url_for('display.home')}), 200
            else:
                return redirect(url_for('display.login', error='Invalid email or password'))
    except Exception as e:
        print(e)
        return redirect(url_for('display.login', error='Something went wrong. Please try again.'))


@userBp.route('/logout', methods=['POST'])
@login_required
def logout():
    try:
        response = jsonify({'message': 'Successfully logged out'})
        logout_user()
        unset_jwt_cookies(response)
        return jsonify({'redirect': url_for('display.index')}), 200
    except Exception as e:
        print(e)
        return jsonify({'error': 'Something went wrong'}), 500