from app import app
from flask import render_template, request, redirect, url_for
from models import *
from flask_login import login_user, logout_user, login_required, current_user
from forms import *
from datetime import datetime
from werkzeug.security import check_password_hash
import xmltodict
import requests


# @app.route("/emanetler/")
# def emanetler():
#     emanet = Universalemanetler.query.all()
#     return render_template("emanetler.html", emanet=emanet)


@app.route("/")
def home():
    date = datetime.now().strftime("%d.%m.%Y")
    r = requests.get(f"https://www.cbar.az/currencies/{date}.xml")
    dict_data = xmltodict.parse(r.content)
    EUR_buy = dict_data["ValCurs"]["ValType"][1]["Valute"][0]["Value"]
    RUB_buy = dict_data["ValCurs"]["ValType"][1]["Valute"][1]["Value"]
    USD_buy = dict_data["ValCurs"]["ValType"][1]["Valute"][2]["Value"]
    GBP_buy = dict_data["ValCurs"]["ValType"][1]["Valute"][3]["Value"]
    EUR_sell = float(EUR_buy)+0.0020
    USD_sell = float(USD_buy)+0.0020
    RUB_sell = float(RUB_buy)+0.0020
    GBP_sell = float(GBP_buy)+0.0020
    return render_template("esas.html", date=date,EUR_sell=EUR_sell, USD_sell=USD_sell, RUB_sell=RUB_sell, GBP_sell=GBP_sell, EUR_buy=EUR_buy, RUB_buy=RUB_buy, USD_buy=USD_buy, GBP_buy=GBP_buy)


@app.route("/xeberler/")
def xeberler():
    xeber = Xeberler.query.all()
    return render_template("xeberler.html", xeber=xeber)


@app.route("/detail/<int:detail_id>/")
def detail(detail_id):
    xeber_detail = Xeberler.query.get_or_404(detail_id)
    return render_template("xeberlerdinamik.html", xeber_detail=xeber_detail)


@app.route("/investisiya/")
def investisiya():
    investisiya_xeberler = Xeberler.query.filter_by(
        kategori="Investisiya").all()
    return render_template("investisiya.html", xeberler=investisiya_xeberler)


@app.route("/maliyye/")
def maliyye():
    maliyye_xeberler = Xeberler.query.filter_by(kategori="Maliyye").all()
    return render_template("maliyye.html", xeberler=maliyye_xeberler)


@app.route("/sosial/")
def sosial():
    sosial_xeberler = Xeberler.query.filter_by(kategori="Sosial").all()
    return render_template("sosial.html", xeberler=sosial_xeberler)


@app.route("/iqtisadi/")
def iqtisadi():
    iqtisadi_xeberler = Xeberler.query.filter_by(kategori="Iqtisadi").all()
    return render_template("iqtisadi.html", xeberler=iqtisadi_xeberler)


@app.route("/emanetler/", methods=['GET', 'POST'])
def emanetler():
    ema=Universalemanetler.query.all()
    
    form=Emanet()
    if request.method == 'POST':
        form=Emanet(request.form)
        if form.validate_on_submit():
            emanetdata=Emanets(name=form.name.data,surname=form.surname.data,phone=form.phone.data,deposit=form.deposit.data)
            emanetdata.save()
    return render_template("emanetler.html", form=form,ema=ema)
        


@app.route('/admin/')
@login_required
def admin():
    return "Admin Paneline Hoş Geldiniz!"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Users.query.filter_by(
            username=username, password=password).first()
        if user:
            login_user(user)
            return redirect('/admin/')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        new_user = Users(username=username,password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('register'))


@app.route('/onlinenovbe', methods=['GET', 'POST'])
def novbe():
    form = OnlineNovbeFormu()
    if request.method == 'POST':
        if form.validate_on_submit():
            contactinfo = onlinenovbe(filial=form.filial.data, xidmet_novu=form.xidmet_novu.data,
                                      tarix=form.tarix.data, vaxt=form.vaxt.data, mobil_nomre=form.mobil_nomre.data)
            contactinfo.save()
    return render_template('onnovbe.html', form=form)


@app.route('/kampaniyalar')
def kampaniyalar():
    kompaniyalar = Kampaniyalar.query.all()
    return render_template('kampaniyalar.html', kompaniyalar=kompaniyalar)


@app.route('/kampaniyalar/detal<int:id>')
def kampaniyalardetali(id):
    kompaniyalar1 = Kampaniyalar.query.filter_by(id=id).first()
    return render_template('kampaniyalar-detal.html', kompaniyalar1=kompaniyalar1)
