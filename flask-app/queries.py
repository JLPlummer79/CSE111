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