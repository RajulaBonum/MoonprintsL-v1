#!/usr/bin/python2

"""
This is the flask app factory - It sets up and instance of the flask
application
"""

from flask import Flask
from config import Config
from app.extensions import db, login_manager, migrate, csrf

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    """ Intialize Flask extensions here """
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    #mail.init_app(app)
    csrf.init_app(app)

    login_manager.login_view = 'auth.login'

    """ Register blueprints here """
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.products import bp as products_bp
    app.register_blueprint(products_bp, url_prefix='/products')

    @app.route('/test/')
    def test_page():
        return '<h1> Testing the flask app factory pattern</h1>'

    return app

@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))