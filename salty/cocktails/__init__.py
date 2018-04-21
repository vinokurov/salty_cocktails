from flask import Flask
from flask_bootstrap import Bootstrap

__author__ = 'vnkrv'

app = Flask('salty')
Bootstrap(app)
# db = SQLAlchemy(app)
app.secret_key = 'devtest'

from salty.cocktails import views