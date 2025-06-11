"""
Authentication routes
"""
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from app.models import User
from app import db

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['POST'])
def login():
    """Login endpoint"""
    data = request.get_json()
    employee_id = data.get('employee_id')
    password = data.get('password')
    
    if not employee_id or not password:
        return jsonify({'message': 'Employee ID and password required'}), 400
    
    user = User.query.filter_by(employee_id=employee_id).first()
    
    if not user or not user.check_password(password):
        return jsonify({'message': 'Invalid credentials'}), 401
    
    if not user.is_active:
        return jsonify({'message': 'Account is deactivated'}), 403
    
    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)
    
    return jsonify({
        'access_token': access_token,
        'refresh_token': refresh_token,
        'user': user.to_dict()
    }), 200

@bp.route('/me', methods=['GET'])
@jwt_required()
def get_current_user():
    """Get current user info"""
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    return jsonify(user.to_dict()), 200

@bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    """Refresh access token"""
    user_id = get_jwt_identity()
    access_token = create_access_token(identity=user_id)
    return jsonify({'access_token': access_token}), 200