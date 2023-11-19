from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False;           #reduces number of error messages

project = SQLAlchemy(app)

class Parks(project.Model):
    iDNumber = project.Column(project.Integer(15), primary_key = True)
    designation = project.Column(project.String(24))
    hours = project.Column(project.String(12))
    totalNumPermits = project.Column(project.Int(5))
    permitType = project.Column(project.String(25))
    name = project.Column(project.String(45))

class Features(project.Model):
    parkIDNumber = project.Column(project.Int(15), primary_key = True)
    featureName = project.Column(project.String(200))
    structures = project.Column(project.String(150))
    flora = project.Column(project.String(200))
    fauna = project.Column(project.String(200))

class Location(project.Model):
    parkIDNumber = project.Column(project.Int(15), primary_key = True)
    state = project.Column(project.String(10))
    address = project.Column(project.String(25))
    county = project.Column(project.String(25))
    city = project.Column(project.String(45))
    zipcode = project.Column(project.Int(14))
      