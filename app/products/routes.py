#!/usr/bin/python3

from flask import render_template, request, url_for, redirect
from app.main import bp


@bp.route('/')
def index():

    return render_template('products/banners.html')

@bp.route('/')
def index():

    return render_template('products/business-cards.html')

@bp.route('/')
def index():

    return render_template('products/hoodies.html')

@bp.route('/')
def index():

    return render_template('products/mugs.html')

@bp.route('/')
def index():

    return render_template('products/t-shirts.html')

@bp.route('/')
def index():

    return render_template('products/water-bottle.html')
