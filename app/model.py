from app import db


class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    phone = db.Column(db.String(64))
    email = db.Column(db.String(64))


class Quest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    text = db.Column(db.String(1024))


class Otziv(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1024))
    name = db.Column(db.String(64))
    name_pdf = db.Column(db.String(64))
    name_img = db.Column(db.String(64))
    type_otz = db.Column(db.Boolean)