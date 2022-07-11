import imp
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "Project"
    
    from .view import view
    from .auth import auth
    
    app.register_blueprint(view, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/auth")

    return app;