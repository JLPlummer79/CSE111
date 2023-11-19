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
      
class Permits(project.Model):
    parkIDNumber = project.Column(project.Int(15), primary_key = True)
    IdNumber = project.Column(project.Int(20), primary_key = True)
    ownerName = project.Column(project.String(45))
    type = project.Column(project.String(25))
    duration = project.Column(project.Int(3))
    startDate = project.Column(project.String(25))
    endDate = project.Column(project.String(25))

class Fees(project.Model):
     parkIDNumber = project.Column( project.Int(15), primary_key = True)
     permitType = project.Column(project.String(24), primary_key = True)
     amount = project.Column(project.Float(15))

class Recreation(project.Model):
    parkIDNumber = project.Column(project.Int(15), primary_key = True)
    permitIDNumber = project.Column(project.Int(20), primay_key = True) 
    activity = project.Column(project.String(25))
    trailName = project.Column(project.String(50))
    trailHead = project.Column(project.String(50))
    road = project.Column(project.String(50))
    campsiteName = project.Column(project.String(50))

class Staff(project.Model):
    employeeIDNumber = project.Column(project.Int(20), primary_key = True)
    parkIDNumber = project.Colum(project.Int(15), primary_key = True)
    department = project.Column(project.String(20))
    schedule = project.Column(project.String(50))
    name = project.Column(project.String(50))