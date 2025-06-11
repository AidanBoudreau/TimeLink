#!/usr/bin/env python3
"""
Entry point for the TimeLink Flask application
"""
import os
from app import create_app

# Create the Flask app
app = create_app(os.getenv('FLASK_ENV', 'development'))

if __name__ == '__main__':
    # Run the application
    app.run(
        host='0.0.0.0',
        port=int(os.getenv('PORT', 5000)),
        debug=app.config.get('DEBUG', True)
    )