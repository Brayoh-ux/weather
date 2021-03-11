from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///weather.db' 

db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)


from app import views