#!/usr/bin/python3

from flask import Blueprint

bp = Blueprint('admin', __name__)

from app.posts import routes
