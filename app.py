
from flask import Flask
from flask import Flask

app = Flask(__name__, template_folder='Templates', static_folder="static")
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:llmmll@127.0.0.1:3306/project"
app.config['SECRET_KEY'] = 'our_project'
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['SECRET_KEY'] = 'RabitaBank'
SQLALCHEMY_TRACK_MOOIFICATIONS = True

from extensions import *
from controllers import *
from models import *


if __name__ == '__main__':
    db.init_app(db)
    db.init_app(migrate)
    app.run(port=5000, debug=True)
