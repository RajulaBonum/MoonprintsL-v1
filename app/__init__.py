#!/usr/bin/python2

"""
This is the flask app factory - It sets up and instance of the flask
application
"""

from flask import Flask
from config import Config
from app.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    """ Intialize Flask extensions here """
    db.init_app(app)

    """ Register blueprints here """
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    @app.route('/test/')
    def test_page():
        return '<h1> Testing the flask app factory pattern</h1>'

    return app
