import sqlite3
from sqlite3 import Error

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
#the basic design pattern for each query; main diff will be
#query and headers that are printed... copy and paste job much 
#of time
#def func_name(_conn): 
#print("++++++++++++++++++++++++++++++++++")
#cur = _conn.cursor()
# try:
#     sql = """ SQL here""" 
# cur.execute(sql)
# l = '{:>10}'.format("Header", "More Headers?")
#print(l)
#print("-------------------------------")
#rows = cur.fetchall()
#for row in rows:
#    l = '{:>10}'.format(row[0], row[1]) match what query returns
#    print(l)
# except Error as e:
#   print(e)
# print("++++++++++++++++++++++++++++++++++")


def printAllParks(_conn):
    print("++++++++++++++++++++++++++++++++++")
    cur = _conn.cursor()
    try:
        sql = """ SELECT name FROM Park;""" 
        cur.execute(sql)
        l = '{:>10}'.format("Park Name")
        print(l)
        print("-------------------------------")
        rows = cur.fetchall()
        for row in rows:
           l = '{:>10}'.format(row[0]) 
           print(l)

    except Error as e:
        print(e)

def parkFeatures(_conn, prk): 
    print("++++++++++++++++++++++++++++++++++")
    cur = _conn.cursor()
    try:
        sql = """ SELECT p.name,f.featureName 
                    FROM Park p, Features f
                    WHERE p.name = ?
                    AND p.iDNumber = f.parkIDNumber;

               """ 
        args = [prk]
        cur.execute(sql,args)
        l = '{:>10} {:>10}'.format("Park", "Features")
        print(l)
        print("-------------------------------")
        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0], row[1]) 
            print(l)
    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def allParkActivities(_conn, _park): 
    print("++++++++++++++++++++++++++++++++++")
    cur = _conn.cursor()
    try:
        sql = """ SELECT p.name, p.permitType
                    FROM Park p
                    WHERE p.name = ?
              """
        args = [_park]
        cur.execute(sql,args)
        l = '{:>10} {:>10}'.format("Name", "Activity")
        print(l)
        print("-------------------------------")
        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0], row[1]) 
            print(l)
    except Error as e:
        print(e)
    
    print("++++++++++++++++++++++++++++++++++")

def printParkFee(_conn, _act, _park):
    cur = _conn.cursor()
    print("++++++++++++++++++++++++++++++++++")

    try:
        sql = """SELECT Fees.amount, Fees.permitType, Park.name
                    FROM Park, Fees
                    WHERE Park.iDNumber = Fees.parkIDNumber
                    AND Fees.permitType = ?
                    AND Park.name = ? """
        
        args = [_act, _park]

        cur = _conn.cursor()
        cur.execute(sql, args)

        l = '{:>10} {:>10} {:>10}'.format("Fee", "Activity", "Park")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10} {:>10}'.format(row[0], row[1], row[2])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def parkOprHrs(_conn, _park):
    print("++++++++++++++++++++++++++++++++++")

    try:
        sql = """SELECT Park.hours, Park.name
                    FROM Park
                    WHERE Park.name = ?"""
        
        args = [_park]
        cur = _conn.cursor()
        cur.execute(sql, args)

        l = '{:>10} {:>10}'.format("Hours", "Park")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0], row[1])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def printAllRecreation(_conn): 
    print("++++++++++++++++++++++++++++++++++")
    cur = _conn.cursor()
    try:
        sql = """ SELECT activity FROM Recreation;""" 
        cur.execute(sql)
        l = '{:>10}'.format("Activity")
        print(l)
        print("-------------------------------")
        rows = cur.fetchall()
        for row in rows:
            l = '{:>10}'.format(row[0]) 
            print(l)
    except Error as e:
       print(e)

    print("++++++++++++++++++++++++++++++++++")

def listTrails(_conn, _park):
    print("++++++++++++++++++++++++++++++++++")

    try:
        sql = """SELECT Park.name, Recreation.trailName
                    FROM Park, Recreation
                    WHERE Park.iDNumber = Recreation.parkIDNumber
                    AND Park.name = ?"""
        args = [_park]
        cur = _conn.cursor()
        cur.execute(sql, args)

        l = '{:>10} {:>10}'.format("Park", "Trail")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0], row[1])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def permitsByPark(_conn, _park):

    print("++++++++++++++++++++++++++++++++++")

    try:
        sql = """SELECT p.name, r.permitIDNumber, r.activity
                FROM Park p, Recreation r
                WHERE p.name = ? 
                AND p.iDNumber = r.parkIDNumber
            """
        args = [_park]
        cur = _conn.cursor()
        cur.execute(sql, args)

        l = '{:>10} {:>20} {:>10}'.format("Park", "Permit Id Number", "Activity")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>20} {:>10}'.format(row[0], row[1], row[2])
            print(l)
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

