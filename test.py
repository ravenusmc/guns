#This file I was trying to use sqlAlchemy but I ran into an error that said: ImportError: No module named 'MySQLdb'
#I spent some time trying to fix this error and could not solve it. So, for the time being, going back to 
#mysql.connector. 

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import mysql.connector

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ted:pass@localhost/movies'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

class Movies(db.Model):
  __tablename__ = 'name'
  name = db.Column('name', db.Unicode, primary_key=False)
  age = db.Column('age', db.Integer, primary_key=False)
  id = db.Column('id', db.Integer, primary_key=True)

test = Movies.query.all()
print(test)




