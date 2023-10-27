from flask_sqlalchemy import SQLAlchemy

#Going to abandon this way for CSE-111 is not what is desired

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'

db = SQLAlchemy(app)

class Parks(db.Model):
    iDNumber = db.Column(db.Integer(15), primary_key = True)
    #featureNameFeatures? this one is inherited from Features... so I am not sure here
    designation = db.Column(db.String(24))
    hours = db.Column(db.String(12))
    totalNumPermits = db.Column(db.Int(5))
    permitType = db.Column(db.String(25))
    name = db.Column(db.String(45))