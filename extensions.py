from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin
from app import app

db=SQLAlchemy(app)
migrate = Migrate(app,db)
login_manager=LoginManager(app)
login_manager.login_view = 'login'
admin = Admin(app, name='Rabitabank', template_mode='bootstrap3')
