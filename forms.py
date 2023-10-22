from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired, Length, Email
from models import *


class OnlineNovbeFormu(FlaskForm):
    filial = SelectField('Secin', choices=[
        ('Seçin', 'Seçin'),
        ('Nəsimi filiali (Bül-bül pr.30)', 'Nəsimi filiali (Bül-bül pr.30)'),
        ('Nizami filiali (Sarayevo küç. 26c)',
         'Nizami filiali (Sarayevo küç. 26c)'),
        ('Səbail Filiali (A.Məhərrəmov küç. 33A)',
         'Səbail Filiali (A.Məhərrəmov küç. 33A)'),
        ('Nərimanov filiali (İ.Hidayətzadə küç.49/51)',
         'Nərimanov filiali (İ.Hidayətzadə küç.49/51)'),
        ('Yasamal filiali (Şərifzadə küç.408)',
         'Yasamal filiali(Şərifzadə küç.408)'),
        ('Baş Ofis (Baki şəh.,Nəsimi ray., 28 May küç.3)',
         'Baş Ofis (Baki  şəh.,Nəsimi ray., 28 May küç.3)'),
        ('Sahil filiali (Ə.Rəcəbli küç.3)', 'Sahil filiali (Ə.Rəcəbli küç.3)'),
        ('Xətai filiali (Xocali pr.37)', 'Xətai filiali (Xocali pr.37)'),
        ('Sumqayit filiali (S.Vurğun küç.102)',
         'Sumqayit filiali (S.Vurğun küç.102)'),
        ('Mərkəz filiali (B.Sərdarov küç.,1)',
         'Mərkəz filiali (B.Sərdarov küç.,1)'),
        ('Şirvan filiali (20 yanvar küç.12)', 'Şirvan filiali (20 yanvar küç.12)'),
        ('Kürdəmir filiali (H.Əliyev pr. 3-cü məh. 50)',
         'Kürdəmir filiali(H.Əliyev pr. 3-cü məh. 50)'),
        ('Ağsu filiali (M.Rəsulzadə küç.35)', 'Ağsu filiali (M.Rəsulzadə küç.35)'),
        ('Şamaxi filiali (N. Nərimanov küç. 66)',
         'Şamaxi  filiali (N. Nərimanov küç. 66)'),
        ('Şəki filiali (M.Rəsulzadə küç.178)',
         'Şəki filiali (M.Rəsulzadə küç.178)'),
        ('Xaçmaz filiali (N.Nərimanov küç.15)',
         'Xaçmaz filiali (N.Nərimanov küç.15)'),
        ('Quba filiali (H.Əliyev pr. və T.Əhmədov küç. kəsişməsi)',
         'Quba filiali (H.Əliyev pr. və T.Əhmədov küç. kəsişməsi)'),
        ('Qusar filiali (N.Şərifov küç. 18A)',
         'Qusar filiali (N.Şərifov küç. 18A)'),
        ('Şəmkir filiali (Nizami Gəncəvi küç.144)',
         'Şəmkir filiali (Nizami Gəncəvi küç.144)'),
        ('Gəncə filiali(H.Əliyev pr. 273)', 'Gəncə filiali(H.Əliyev pr. 273)'),
        ('Ağcabədi filiali (H.Əliyev pr.29)',
         'Ağcabədi filiali  (H.Əliyev pr.29)'),
        ('Lənkəran filiali (Mir Mustafaxan küç.33)',
         'Lənkəran filiali (Mir Mustafaxan küç.33)'),
        ('Masalli filiali (H.Əliyev pr. və H.Aslanov küç. kəsişməsi)',
         'Masalli filiali (H.Əliyev pr. və H.Aslanov küç. kəsişməsi)'),
        ('Kaspian filiali (C. Cabbarli küç.44(Caspian Plaza))',
         'Kaspian filiali (C. Cabbarli küç.44(Caspian Plaza))'),
        ('KOB Mərkəzi (Ə.Rəcəbli -3 küç., 5)',
         'KOB Mərkəzi (Ə.Rəcəbli -3 küç., 5)'),
        ('Naxçivan filiali(H.Əliyev pros.3/13)',
         'Naxçivan filiali (H.Əliyev pros.3/13)'),
    ], validators=[DataRequired()])

    xidmet_novu = SelectField('Secin', choices=[
        ('Seçin', 'Seçin'),
        ('Kredit müraciəti', 'Kredit müraciəti'),
        ('Sürətli pul köçürmələri', 'Sürətli pul köçürmələri'),
        ('Plastik kart', 'Plastik kart'),
        ('Əmanət', 'Əmanət'),
        ('Hesab üzrə əməliyyatlar', 'Hesab üzrə əməliyyatlar'),
        ('Hüquqi şəxs və sahibkarlar', 'Hüquqi şəxs və sahibkarlar'),
    ], validators=[DataRequired()])

    tarix = SearchField('Seçilen Tarix', validators=[DataRequired()], render_kw={
                        'class': 'novbe_6', 'type': 'date', 'id': 'birthday'})

    vaxt = SelectField('Secin', choices=[
        ('Seçin', 'Seçin'),
        ('09:00:00', '09:00:00'),
        ('10:00:00', '10:00:00'),
        ('11:00:00', '11:00:00'),
        ('12:00:00', '12:00:00'),
        ('14:00:00', '14:00:00'),
        ('15:00:00', '15:00:00'),
        ('16:00:00', '16:00:00')
    ], validators=[DataRequired()])

    mobil_nomre = SearchField('Mobil nömrəniz', validators=[DataRequired()], render_kw={
                              'class': 'novbe_6', 'style': 'padding-left: 20px;', 'inputmode': 'tel', 'placeholder': 'məs: 0702434343'})


class Emanet(FlaskForm):
    name = StringField(validators=[DataRequired()],render_kw={'class':'from-control',})
    surname = StringField(validators=[DataRequired()])
    phone = StringField(validators=[DataRequired()])
    deposit = RadioField(choices=[('Universal Əmanət', 'Universal Əmanət'), (
        'Uşaq Yığım Əmanəti', 'Uşaq Yığım Əmanəti'), ('Saxlanc Seyfləri', 'Saxlanc Seyfləri')])
