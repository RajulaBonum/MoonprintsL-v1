#!/usr/bin/python3

from app.extensions import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    """This will represent the user information """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)


    def __repr__(self):
        return f'<User {self.username}>'


class Product(db.Model):
    """This model will represent the products"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<Product {self.name}>'
        
