from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt_identity

def role_required(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            identity = get_jwt_identity()
            print(identity)
            print(role)
            print(identity['role'])

            if role == identity['role']:
                return func(*args, **kwargs)

            return jsonify({'error': 'Access denied'}), 403
        return wrapper
    return decorator

# @role_required('user')
# def view_product(id):
# .....
