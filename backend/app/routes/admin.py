"""
Admin routes
"""
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint('admin', __name__)

@bp.route('/dashboard', methods=['GET'])
@jwt_required()
def dashboard():
    """Admin dashboard endpoint"""
    return jsonify({
        'message': 'Admin dashboard',
        'user_id': get_jwt_identity()
    }), 200

@bp.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    """Get all users endpoint"""
    return jsonify({'message': 'Users list endpoint - to be implemented'}), 200