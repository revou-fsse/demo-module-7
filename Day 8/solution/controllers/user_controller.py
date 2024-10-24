import datetime
from flask import Blueprint, jsonify, request
from sqlalchemy import text
from models.user_model import UserModel
from connectors.db import Session
from flask_jwt_extended import jwt_required, create_access_token
from services.user_service import role_required

userBp = Blueprint('userBp', __name__)

@userBp.route('/user/login', methods=['POST'])
def user_login():
    data = request.get_json()

    if data is None:
        return jsonify({'error': 'No data received'})
    
    if 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Missing required fields'})
    
    with Session() as session:
        try:
            user = session.query(UserModel).filter(UserModel.email == data['email']).first()
            session.execute(text('SELECT * FROM users where email = email and password = password'), {
                'email': data['email'],
                'password': data['password']
            })

            if user and user.check_password(data['password']):
                expires = datetime.timedelta(minutes=60)
                access_token = create_access_token(identity={
                    'user_id': user.user_id,
                    'name': user.name,
                    'role': user.role
                }, expires_delta=expires)
                return jsonify({
                    'message': f'User {user.name} logged in successfully',
                    'access_token': access_token
                }), 201
            
            return jsonify({'error': 'Invalid email or password'}), 400
        except Exception as e:
            print(e)
            return jsonify({'error': 'Failed to login user'}), 500
        

@userBp.route('/user/register', methods=['POST'])
def user_register():
    data = request.get_json()

    if data is None:
        return jsonify({'error': 'No data received'}), 400
    
    if 'name' not in data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
    
    with Session() as session:
        try:
            user = UserModel(name=data['name'], email=data['email'], role=data['role'])
            user.set_password(data['password'])

            session.add(user)
            session.commit()
            return jsonify({'message': f'User {user.name} created successfully'})
        except Exception as e:
            print(e)
            session.rollback()
            return jsonify({'error': 'Failed to create user'}), 500
        


@userBp.route('/user/all', methods=['GET'])
@jwt_required()
def user_all():
    with Session() as session:
        users = session.query(UserModel).all()
        return jsonify([{ 'user_id': user.user_id, 'name': user.name, 'email': user.email } for user in users])
    
@userBp.route('/user/asep', methods=['GET'])
@jwt_required()
@role_required('admin')
def user_asep():
    with Session() as session:
        users = session.query(UserModel).all()
        return jsonify([{ 'user_id': user.user_id, 'name': user.name, 'email': user.email } for user in users])
    