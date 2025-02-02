#!/usr/bin/python3

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hey_i_am_secret'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
            or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
