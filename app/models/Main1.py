#!/usr/bin/python3

from app.extensions import db

class Main1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hero_h1 = db.Column(db.String(255))
    hero_h2 = db.Column(db.String(255))
    #Products section
    products_h1 = db.Column(db.String(255))
    products_item1_h1 = db.Column(db.String(255))
    products_item1_p = db.Column(db.Text)
    products_item2_h1 = db.Column(db.String(255))
    products_item2_p = db.Column(db.Text)
    products_item3_h1 = db.Column(db.String(255))
    products_item3_p = db.Column(db.Text)
    products_item4_h1 = db.Column(db.String(255))
    products_item4_p = db.Column(db.Text)

    #Abouts section
    about_h1 = db.Column(db.String(255))
    about_p = db.Column(db.String(255))
    about_cntc_c1 = db.Column(db.String(255))
    about_cntc_c2 = db.Column(db.String(255))
    about_cntc_l1 = db.Column(db.String(255))
    about_cntc_l2 = db.Column(db.String(255))
    about_cntc_hp = db.Column(db.String(255))

    #Value Proposition section
    value_h1 = db.Column(db.String(255))
    value_item1_h = db.Column(db.String(255))
    value_item1_p = db.Column(db.Text)
    value_item2_h = db.Column(db.String(255))
    value_item2_p = db.Column(db.Text)
    value_item3_h = db.Column(db.String(255))
    value_item3_p = db.Column(db.Text)



    def __repr__(self):
        return f'<Main1 "{self.id}">'
