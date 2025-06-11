"""
Manager routes
"""
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint('manager', __name__)

@bp.route('/dashboard', methods=['GET'])
@jwt_required()
def dashboard():
    """Manager dashboard endpoint"""
    return jsonify({
        'message': 'Manager dashboard',
        'user_id': get_jwt_identity()
    }), 200

@bp.route('/reports', methods=['GET'])
@jwt_required()
def reports():
    """Get reports endpoint"""
    return jsonify({'message': 'Reports endpoint - to be implemented'}), 200