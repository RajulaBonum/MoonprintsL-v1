#!/usr/bin/python3

from flask import render_template, request, url_for, redirect
from app.main import bp


@bp.route('/')
def index():

    return render_template('index.html')

@bp.route('/about')
def about():

    return render_template('about.html')

@bp.route('/contact')
def contact():

    return render_template('contact.html')