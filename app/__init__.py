import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_marshmallow import Marshmallow


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['JWL_SECRET_KEY'] = os.environ.get('JWL_SECRET_KEY')


db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

load_dotenv()

from app.views import view

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
