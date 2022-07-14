from os import path
from venv import create
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
DB_name = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "Project"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_name}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    
    from .view import view
    from .auth import auth
    
    app.register_blueprint(view, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/auth")
    
    from .models import User

    create_database(app=app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app;


def create_database(app):
    if not path.exists('website/'+DB_name):
        db.create_all(app=app)
        print('Created Database')