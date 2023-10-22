from extensions import *
from flask import redirect, request, url_for
from flask_login import UserMixin, current_user
from flask_admin.contrib.sqla import ModelView
from werkzeug.security import generate_password_hash, check_password_hash

from app import app


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save(self):
        db.session.add(self)
        db.session.commit()


class Kampaniyalar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    date = db.Column(db.String(25))
    date1 = db.Column(db.String(25))
    date2 = db.Column(db.String(25))
    comment = db.Column(db.Text)
    image = db.Column(db.Text, nullable=True)
    kategori = db.Column(db.String(255))

    def __repr__(self):
        return self.name

    def __init__(self, name, date, date1, date2, comment, image, kategori):
        self.name = name
        self.date = date
        self.date1 = date1
        self.date2 = date2
        self.comment = comment
        self.image = image
        self.kategori = kategori


class onlinenovbe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filial = db.Column(db.String(100))
    xidmet_novu = db.Column(db.String(100))
    tarix = db.Column(db.String(100))
    vaxt = db.Column(db.String(100))
    mobil_nomre = db.Column(db.String(100))

    def __repr__(self):
        return self.filial

    def __init__(self, filial, xidmet_novu, tarix, vaxt, mobil_nomre):
        self.filial = filial
        self.xidmet_novu = xidmet_novu
        self.tarix = tarix
        self.vaxt = vaxt
        self.mobil_nomre = mobil_nomre


class Universalemanetler(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    basliq = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    muddet = db.Column(db.String(255), nullable=False)
    faiz = db.Column(db.String(255), nullable=False)
    valyuta = db.Column(db.String(255), nullable=False)
    img = db.Column(db.String(255), nullable=False)

    def __init__(self, basliq, description, muddet, faiz, valyuta, img):
        self.basliq = basliq
        self.description = description
        self.muddet = muddet
        self.faiz = faiz
        self.valyuta = valyuta
        self.img = img

    def save(self):
        db.session.add(self)
        db.session.commit()


class Xeberler(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    basliq = db.Column(db.String(255), nullable=False)
    img = db.Column(db.String(255), nullable=False)
    tarix = db.Column(db.String(255), nullable=False)
    kategori = db.Column(db.String(255))
    details = db.Column(db.Text)
    details_img = db.Column(db.String(255))

    def __init__(self, basliq, img, tarix, kategori, details, details_img):
        self.basliq = basliq
        self.img = img
        self.tarix = tarix
        self.kategori = kategori
        self.details = details
        self.details_img = details_img

    def save(self):
        db.session.add(self)
        db.session.commit()


class Emanets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    deposit = db.Column(db.Text(), nullable=False)

    def __init__(self, name, surname, phone, deposit):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.deposit = deposit

    def save(self):
        db.session.add(self)
        db.session.commit()


class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login', next=request.url))


admin.add_view(MyModelView(Universalemanetler, db.session))
admin.add_view(MyModelView(Xeberler, db.session))
admin.add_view(MyModelView(Emanets, db.session))
admin.add_view(MyModelView(Users, db.session))






