from flask import Flask, render_template
import sqlite3
from sqlite3 import Error
#from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.ext.automap import automap_base
#from sqlalchemy.orm import Session
#from sqlalchemy import create_engine
#import string
#from decimal import Decimal
#import os

app = Flask(__name__)

def openConnection(_dbFile):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn

def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


@app.route('/')
def index():
    database = r"project.db"
    con = openConnection(database)
    cur = con.cursor()
    
    try:
        sql = """
            SELECT * FROM Park;
        """
        cur.execute(sql)
        tests =  cur.fetchall()
        l = '{:>10} {:>10} {:>10} {:>10} {:>10}'.format("Name", "Designation", "Address", "City", "Zip Code")
        print(l)
        print("-------------------------------")

        for row in tests:
            l = '{:>10} {:>10} {:>10} {:>10} {:>10}'.format(row[0], row[1], row[2], row[3], row[4])
            print(l)

    except Error as e:
        print(e)

    closeConnection(con, database)

    return render_template('index.html', tests=tests)

#@app.route('/<name>/<email>')
#def index(name,email):
#     user = User(username=name, email=email)
#     db.session.add(user)
#     db.session.commit()
#     return '<h1>Added new user</h1>'


def main():
    database = r"project.db"
    con = openConnection(database)
    closeConnection(con, database)

if __name__ == '__main__':
    #create_app()
    app.run()
