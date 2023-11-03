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


def createTables(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create tables")

    try:
        sql = """CREATE TABLE Park( iDNumber Int(15) PRIMARY KEY, 
                    designation Varchar(24), 
                    hours Varchar(12), 
                    totalNumPermits Int(5), 
                    permitType Varchar(25), 
                    name Varchar(45) NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE Location ( parkIDNumber Int(15) PRIMARY KEY, 
                    state varchar(10), 
                    address varchar(25), 
                    county varchar(25), 
                    city varchar(45), 
                    zipcode Int(14) NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE Features( parkIDNumber Int(15) PRIMARY KEY, 
                    featureName varchar(200), 
                    structures varchar(150), 
                    flora varchar(200), 
                    fauna varchar(200) NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE Permits( parkIDNumber Int(15) PRIMARY KEY, 
                    IdNumber Int(20), 
                    ownerName varchar(45), 
                    type varchar(25), 
                    duration int(3), 
                    startDate TEXT, 
                    endDate TEXT NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE Fees( parkIDNumber Int(15) PRIMARY KEY, 
                    permitType varchar(24), 
                    amount decimal(15) NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE Recreation( parkIDNumber Int(15) PRIMARY KEY, 
                    permitIDNumber Int(20), 
                    activity varchar(25), 
                    trailName varchar(50), 
                    trailHead varchar(50), 
                    road varchar(50), 
                    campsiteName varchar(50) NOT NULL)"""
        _conn.execute(sql)

        sql = """CREATE TABLE Staff(employeeIDNumber Int(20) PRIMARY KEY, 
                    parkIDNumber Int(15) PRIMARY KEY, 
                    department varchar(20), 
                    schedule varchar(50),
                    name varchar(50) NOT NULL);"""

        _conn.execute(sql)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def dropTables(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Drop tables")

    try:
        sql = "DROP TABLE Park"
        _conn.execute(sql)

        sql = "DROP TABLE Features"
        _conn.execute(sql)

        sql = "DROP TABLE Fees"
        _conn.execute(sql)

        sql = "DROP TABLE Permits"
        _conn.execute(sql)

        sql = "DROP TABLE Location"
        _conn.execute(sql)

        sql = "DROP TABLE Recreation"
        _conn.execute(sql)

        sql = "DROP TABLE Staff"
        _conn.execute(sql)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def populateTable_Park(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Park")

    try:
        parks = [
            (1, 'NationalPark', 'M-Sun 8:00 - 17:00', 12, 'hiking-backpacking-camping-swimming', 'Yellowstone'),
            (2, 'NationalPark', 'Sun-Sat 8:00 - 17:00', 42, 'hiking-backpacking-camping-swimming-rockclimbing', 'Yosemite'),
            (3, 'NationalPark', 'Sun-Sat 8:00 - 17:00', 42, 'hiking-backpacking-camping-rockclimbing', 'Arches'),
            (4, 'NationalPark', 'Sun-Sat 8:00 - 17:00', 42, 'hiking-camping-swimming', 'Acadia'),
            (5, 'NationalPark', 'Sun-Sat 8:00 - 17:00', 42, 'hiking-camping-swimming-rafting-backpacking-rockclimbing-fishing', 'Grand Canyon'),
            (6, 'NationalMonument', 'Sun-Sat 8:00 - 17:00', 500, 'hiking-camping-backpacking-rockclimbing', 'Mojave'),
            (7, 'NationalMonument', 'Sun-Sat 8:00 - 17:00', 500, 'hiking-rockclimbing', 'Devils Postpile'),
            (8, 'NationalSeashore', 'Sun-Sat 8:00 - 17:00', 457, 'hiking-swimming-fishing', 'Point Reyes'),
            (9, 'NationalSeashore', 'Sun-Sat 8:00 - 17:00', 457, 'hiking-swimming-fishing', 'Padre Island'),
            (10, 'NationalMonument', 'Sun-Sat 8:00 - 17:00', 500, 'hiking', 'Cabrillo'),
            (11, 'NationalPark', 'Sun-Sat 8:00 - 17:00', 27, 'hiking-camping-backpacking', 'Badlands'),
            (12, 'NationalPark', 'Sun-Sat 8:00 - 17:00', 634, 'hiking-camping-backpacking-rockclimbing-mountaineering', 'Rocky Mountain'),
            (13, 'NationalPark', 'Sun-Sat 8:00 - 17:00', 439, 'hiking-camping-backpacking', 'Olympic'),
            (14, 'NationalPark', 'Sun-Sat 8:00 - 17:00', 350, 'hiking-camping-backpacking', 'Great Sand Dunes'),
            (15, 'NationalPark', 'Sun-Sat 8:00 - 17:00', 475, 'hiking-camping-backpacking', 'Great Smokey Mountains'),
            (16, 'NationalPark', 'Sun-Sat 8:00 - 17:00', 475, 'hiking-camping-backpacking-fishing', 'Shenandoah'),
            (17, 'NationalMonument', 'Sun-Sat 8:00 - 17:00', 500, 'hiking', 'Statue of Liberty'),
            (18, 'NationalMonument', 'Sun-Sat 8:00 - 17:00', 58, 'hiking', 'John Day Fossil Beds'),
            (19, 'NationalMonument', 'Sun-Sat 8:00 - 17:00', 101, 'hiking', 'Rainbow Bridge'),
            (20, 'NationalSeashore', 'Sun-Sat 8:00 - 17:00', 457, 'hiking-swimming-fishing', 'Cape Cod'),
            (21, 'NationalSeashore', 'Sun-Sat 8:00 - 17:00', 87, 'hiking-swimming-fishing', 'Assateague Island')
        ]

        sql = "INSERT INTO Park VALUES(?, ?, ?)"
        _conn.executemany(sql, parks)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def insert_Fee(_conn, _parkID, _permitType, _amt):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert Fee")

    try:
        sql = """INSERT INTO Fees(parkIDNumber, permitType, amount)
            VALUES(?, ?, ?)"""
        args = [_parkID, _permitType, _amt]
        _conn.execute(sql, args)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def populateTable_Fees(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate PC")

    
    insert_Fee(1, 'hiking', 15.00)
    insert_Fee(1, 'backpacking', 20.00)
    insert_Fee(1, 'camping', 17.00)
    insert_Fee(1, 'swimming', 16.00)
    insert_Fee(1, 'fishing', 13.00)
    insert_Fee(2, 'hiking', 15.00)
    insert_Fee(2, 'backpacking', 20.00)
    insert_Fee(2, 'camping', 17.00)
    insert_Fee(2, 'swimming', 16.00)
    insert_Fee(2, 'fishing', 13.00)
    insert_Fee(2, 'rockclimbing', 25.00)
    insert_Fee(3, 'hiking', 15.00)
    insert_Fee(3, 'backpacking', 20.00)
    insert_Fee(3, 'camping', 17.00)
    insert_Fee(3, 'rockclimbing', 25.00)
    insert_Fee(4, 'hiking', 15.00)
    insert_Fee(4, 'camping', 22.00)
    insert_Fee(4, 'swimming', 10.00)
    insert_Fee(5, 'hiking', 10.00)
    insert_Fee(5, 'camping', 19.50)
    insert_Fee(5, 'backpacking', 15.00)
    insert_Fee(5, 'fishing', 8.00)
    insert_Fee(5, 'rafting', 45.00)
    insert_Fee(5, 'rockclimbing', 30.00)
    insert_Fee(5, 'swimming', 5.00)
    insert_Fee(6, 'camping', 6.00)
    insert_Fee(6, 'hiking', 9.00)
    insert_Fee(6, 'backpacking', 6.00)
    insert_Fee(6, 'rockclimbing', 22.00)
    insert_Fee(7, 'rockclimbing', 15.00)
    insert_Fee(7, 'hiking', 7.00)
    insert_Fee(8, 'hiking', 7.00)
    insert_Fee(8, 'swimming', 5.00)
    insert_Fee(8, 'fishing', 12.00)
    insert_Fee(9, 'hiking', 15.00)
    insert_Fee(9, 'swimming', 20.00)
    insert_Fee(9, 'fishing', 15.00)
    insert_Fee(10, 'hiking', 5.00)
    insert_Fee(11, 'hiking', 8.00)
    insert_Fee(11, 'camping', 18.00)
    insert_Fee(11, 'backpacking', 10.00)

    insert_Fee(12, 'rockclimbing', 35.00)
    insert_Fee(12, 'camping', 15.00)
    insert_Fee(12, 'backpacking', 12.00)
    insert_Fee(12, 'hiking', 10.00)
    insert_Fee(12, 'mountaineering', 40.00)
    insert_Fee(13, 'hiking', 12.00)
    insert_Fee(13, 'camping', 22.00)
    insert_Fee(13, 'backpacking', 12.00)
    insert_Fee(14, 'hiking', 12.00)
    insert_Fee(14, 'camping', 24.00)
    insert_Fee(14, 'backpacking', 12.00)
    insert_Fee(15, 'hiking', 9.00)
    insert_Fee(15, 'camping', 25.00)
    insert_Fee(15, 'backpacking', 12.00)
    insert_Fee(16, 'hiking', 8.00)
    insert_Fee(16, 'camping', 21.00)
    insert_Fee(16, 'backpacking', 9.00)
    insert_Fee(16, 'fishing', 21.50)
    insert_Fee(17, 'hiking', 19.00)
    insert_Fee(18, 'hiking', 14.00)
    insert_Fee(19, 'hiking', 12.00)
    insert_Fee(20, 'hiking', 10.00)
    insert_Fee(20, 'swimming', 8.00)
    insert_Fee(20, 'fishing', 15.00)
    insert_Fee(21, 'hiking', 17.00)
    insert_Fee(21, 'swimming', 5.00)
    insert_Fee(21, 'fishing', 12.00)

    print("success")
    print("++++++++++++++++++++++++++++++++++")


# def insert_Laptop(_conn, _model, _speed, _ram, _hd, _screen, _price):
#     print("++++++++++++++++++++++++++++++++++")
#     print("Insert Laptop")

#     try:
#         sql = "INSERT INTO Laptop VALUES(?, ?, ?, ?, ?, ?)"
#         args = [_model, _speed, _ram, _hd, _screen, _price]
#         _conn.execute(sql, args)

#         _conn.commit()
#         print("success")
#     except Error as e:
#         _conn.rollback()
#         print(e)

#     print("++++++++++++++++++++++++++++++++++")


# def populateTable_Laptop(_conn):
#     print("++++++++++++++++++++++++++++++++++")
#     print("Populate Laptop")

#     insert_Laptop(_conn, 2001, 2.00, 2048, 240, 20.1, 3673)
#     insert_Laptop(_conn, 2002, 1.73, 1024, 80, 17.0, 949)
#     insert_Laptop(_conn, 2003, 1.80, 512, 60, 15.4, 549)
#     insert_Laptop(_conn, 2004, 2.00, 512, 60, 13.3, 1150)
#     insert_Laptop(_conn, 2005, 2.16, 1024, 120, 17.0, 2500)
#     insert_Laptop(_conn, 2006, 2.00, 2048, 80, 15.4, 1700)
#     insert_Laptop(_conn, 2007, 1.83, 1024, 120, 13.3, 1429)
#     insert_Laptop(_conn, 2008, 1.60, 1024, 100, 15.4, 900)
#     insert_Laptop(_conn, 2009, 1.60, 512, 80, 14.1, 680)
#     insert_Laptop(_conn, 2010, 2.00, 2048, 160, 15.4, 2300)

#     print("success")
#     print("++++++++++++++++++++++++++++++++++")


# def insert_Printer(_conn, _model, _color, _type, _price):
#     print("++++++++++++++++++++++++++++++++++")
#     print("Insert Printer")

#     try:
#         sql = """INSERT INTO Printer(model, color, type, price)
#                 VALUES(?, ?, ?, ?)"""
#         args = [_model, _color, _type, _price]
#         _conn.execute(sql, args)

#         _conn.commit()
#         print("success")
#     except Error as e:
#         _conn.rollback()
#         print(e)

#     print("++++++++++++++++++++++++++++++++++")


# def populateTable_Printer(_conn):
#     print("++++++++++++++++++++++++++++++++++")
#     print("Populate Printer")

#     insert_Printer(_conn, 3001, True, "ink-jet", 99)
#     insert_Printer(_conn, 3002, False, "laser", 239)
#     insert_Printer(_conn, 3003, True, "laser", 899)
#     insert_Printer(_conn, 3004, True, "ink-jet", 120)
#     insert_Printer(_conn, 3005, False, "laser", 120)
#     insert_Printer(_conn, 3006, True, "ink-jet", 100)
#     insert_Printer(_conn, 3007, True, "laser", 200)

#     print("success")
#     print("++++++++++++++++++++++++++++++++++")


# def populateTables(_conn):
#     #populateTable_Park(_conn)
#     #populateTable_Fees(_conn)
#     # populateTable_Laptop(_conn)
#     # populateTable_Printer(_conn)


def parksAllowSwimming(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Parks that allow swimming")

    try:
        sql = """SELECT name 
                FROM Park 
                WHERE permitType 
                LIKE '%swimming%'"""
        cur = _conn.cursor()
        cur.execute(sql)
        l = '{:>10}'.format("park")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10}'.format(row[0])
            print(l)
    
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def cmpPermitsFees(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Print owners and fees of camping permits from Yosemite.")
    try:
        sql = """SELECT ownerName, amount FROM Permits, Fees
                    WHERE Permits.type = Fees.permitType
                    AND Permits.parkIDNumber = Fees.parkIDNumber
                    AND Permits.type LIKE '%camping%'
                    AND Fees.parkIDNumber = 2"""
        cur = _conn.cursor()
        cur.execute(sql)
        l = '{:>10} {:>10}'.format("owner", "fee")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0], row[1])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def parksHvBearsCamping(_conn):
    print("++++++++++++++++++++++++++++++++++")

    print("Parks that have bears and allow camping.")

    try:
        sql = """SELECT name FROM Park, Features
                    WHERE parkIDNumber = iDNumber
                    AND Features.fauna LIKE '%Bear%'
                    AND Park.permitType LIKE '%camping%'"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        l = '{:>10}'.format("parks")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10}'.format(row[0])
            print(l)
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def actInShenandoah(_conn):
    print("++++++++++++++++++++++++++++++++++")

    print("Display all activities in Shenandoah National Park.")

    try:
        sql = """SELECT permitType  
                    FROM Park
                    WHERE Park.name = 'Shenandoah'"""
        cur = _conn.cursor()
        cur.execute(sql)
        l = '{:>10}'.format("Activities")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10}'.format(row[0])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def typesOfPark(_conn):
    print("++++++++++++++++++++++++++++++++++")

    print("Names and Designations of all parks in CA")

    try:
        sql = """SELECT DISTINCT name, designation, address, city, zipcode
                    FROM Park, Location
                    WHERE Location.state = 'California'
                    AND Location.parkIdNumber = Park.iDNumber"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        l = '{:>10} {:>10} {:>10}'.format("Name", "Designation", "Address")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10} {:>10}'.format(row[0], row[1], row[2])
            print(l)        

    except Error as e:
        print(e)



    print("++++++++++++++++++++++++++++++++++")

def countStaff(_conn):
    print("++++++++++++++++++++++++++++++++++")

    print("Print number of staff at each park.")

    try:
        sql = """SELECT DISTINCT Park.name, COUNT(s.employeeIDNumber) 
                        FROM Staff s, Park
                        WHERE Park.IDNumber = s.parkIDNumber
                        GROUP BY s.parkIDNUMBER"""
        cur = _conn.cursor()
        cur.execute(sql)
        l = '{:>10} {:>10}'.format("Park Name", "Staffing Count")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0], row[1])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")



# def pcsByMaker(_conn, _maker):
#     print("++++++++++++++++++++++++++++++++++")
#     print("PCs by maker: ", _maker)

#     try:
#         sql = """select P.model as model, PC.price as price
#                 from Product P, PC
#                 where P.model = PC.model AND
#                 maker = ?"""
#         args = [_maker]

#         cur = _conn.cursor()
#         cur.execute(sql, args)

#         l = '{:>10} {:>10}'.format("model", "price")
#         print(l)
#         print("-------------------------------")

#         rows = cur.fetchall()
#         for row in rows:
#             l = '{:>10} {:>10}'.format(row[0], row[1])
#             print(l)

#     except Error as e:
#         print(e)

#     print("++++++++++++++++++++++++++++++++++")


# def productByMaker(_conn, _pType, _maker):
#     print("++++++++++++++++++++++++++++++++++")
#     print(_pType, " by maker: ", _maker)

#     try:
#         sql = """select P.model as model,
#             {}.price as price
#             from Product P, {}
#             where P.model = {}.model AND
#             maker = ?""".format(_pType, _pType, _pType)
#         args = [_maker]

#         cur = _conn.cursor()
#         cur.execute(sql, args)

#         l = '{:>10} {:>10}'.format("model", "price")
#         print(l)
#         print("-------------------------------")

#         rows = cur.fetchall()
#         for row in rows:
#             l = '{:>10} {:>10}'.format(row[0], row[1])
#             print(l)

#     except Error as e:
#         print(e)

#     print("++++++++++++++++++++++++++++++++++")


# def allProductsByMaker(_conn, _maker):
#     print("++++++++++++++++++++++++++++++++++")
#     print("Products by maker: ", _maker)

#     try:
#         sql = """select P.model as model, P.type as type, PC.price as price
#             from Product P, PC
#             where P.model = PC.model AND
#             maker = ?
#             UNION
#             select P.model as model, P.type as type, L.price as price
#             from Product P, Laptop L
#             where P.model = L.model AND
#             maker = ?
#             UNION
#             select P.model as model, P.type as type, Pr.price as price
#             from Product P, Printer Pr
#             where P.model = Pr.model AND
#             maker = ?"""
#         args = [_maker, _maker, _maker]

#         cur = _conn.cursor()
#         cur.execute(sql, args)

#         l = '{:>10} {:>20} {:>10}'.format("model", "type", "price")
#         print(l)
#         print("-------------------------------")

#         rows = cur.fetchall()
#         for row in rows:
#             l = '{:>10} {:>20} {:>10}'.format(row[0], row[1], row[2])
#             print(l)

#     except Error as e:
#         print(e)

#     print("++++++++++++++++++++++++++++++++++")


def main():
    database = r"project.db"

    # create a database connection
    conn = openConnection(database)
    with conn:
        #dropTables(conn)
        #createTables(conn)
        #populateTables(conn)
        parksAllowSwimming(conn)
        cmpPermitsFees(conn)
        parksHvBearsCamping(conn)
        actInShenandoah(conn)
        typesOfPark(conn)
        countStaff(conn)

      #  pcsByMaker(conn, "E")
      #  productByMaker(conn, "Laptop", "E")
      #  allProductsByMaker(conn, "E")

        closeConnection(conn, database)


if __name__ == '__main__':
    main()
