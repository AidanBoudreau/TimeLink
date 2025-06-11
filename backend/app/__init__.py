"""
Flask application factory for TimeLink
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from config import config

# Initialize extensions
db = SQLAlchemy()
cors = CORS()
login_manager = LoginManager()
jwt = JWTManager()


def create_app(config_name='default'):
    """Create and configure the Flask application"""
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    # Initialize extensions
    db.init_app(app)
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})
    login_manager.init_app(app)
    jwt.init_app(app)
    
    # Configure login manager
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page.'
    
    # Register blueprints
    from app.routes import auth, employee, manager, admin
    app.register_blueprint(auth.bp, url_prefix='/api/auth')
    app.register_blueprint(employee.bp, url_prefix='/api/employee')
    app.register_blueprint(manager.bp, url_prefix='/api/manager')
    app.register_blueprint(admin.bp, url_prefix='/api/admin')
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    @app.route('/api/health')
    def health_check():
        return {'status': 'healthy', 'message': 'TimeLink API is running'}
    
    return app