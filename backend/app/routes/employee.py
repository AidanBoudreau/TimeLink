"""
Employee routes
"""
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint('employee', __name__)

@bp.route('/dashboard', methods=['GET'])
@jwt_required()
def dashboard():
    """Employee dashboard endpoint"""
    return jsonify({
        'message': 'Employee dashboard',
        'user_id': get_jwt_identity()
    }), 200

@bp.route('/clock-in', methods=['POST'])
@jwt_required()
def clock_in():
    """Clock in endpoint"""
    return jsonify({'message': 'Clock in endpoint - to be implemented'}), 200

@bp.route('/clock-out', methods=['POST'])
@jwt_required()
def clock_out():
    """Clock out endpoint"""
    return jsonify({'message': 'Clock out endpoint - to be implemented'}), 200