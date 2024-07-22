#!/usr/bin/python3

from flask import render_template, request, url_for, redirect
from app.questions import bp
from app.models.question import Question
from app.extensions import db


@bp.route('/', methods=('GET', 'POST'))
def index():
    main1 = Main1.query.all()

    if request.method == 'POST':
        new_main = Main1(content=request.form['content'],
                                answer=request.form['answer'])
        db.session.add(new_main)
        db.session.commit()
        return redirect(url_for('admin.index'))

    return render_template('admin/index.html', main1=main1)
