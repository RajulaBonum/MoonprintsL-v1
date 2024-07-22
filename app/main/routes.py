#!/usr/bin/python3

from flask import render_template, request, url_for, redirect
from app.main import bp


@bp.route('/')
def index():
    
    main1 = Main1.query.all()

    return render_template('index.html', main1=main1)
