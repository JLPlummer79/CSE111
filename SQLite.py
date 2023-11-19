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

def insert_Features(_conn, _parkId, _featureName, _structures, _flora, _fauna):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert Features")

    try:
           sql = """INSERT INTO Features(parkIdNumber, featureName, structures, flora, fauna)
               VALUES(?, ?, ?, ?, ?)"""
           args = [_parkId, _featureName, _structures, _flora, _fauna]
           _conn.execute(sql, args)
           _conn.commit()
           print("successs")
    except Error as e:
           _conn.rollback()
           print(e)
    print("++++++++++++++++++++++++++++++++++")

def populateTable_Features (_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Features")
    insert_Features(1, 'Old Faithful-Grand Prismatic-Yellowstone Falls-Mudpots', 'visitor centers-hotels-bathrooms-gift shops', 'Lodgepole Pine', 'Bison-Elk-Grizzley Bear-Wolf')
    insert_Features(2, 'Half Dome-Vernal Falls-Upper+Lower Yosemite Falls-Vernal Falls', 'visitor centers-hotels-bathrooms-gift shops', 'Lodgepole Pine', 'Brown Bear-Raccoon-Deer-Chipmunk')
    insert_Features(3, 'Delicate Arch-Windows-Great Wall-Courthouse', 'visitor center-bathrooms-gift shop', 'Chaparael', 'Coyote-Alligator Lizard')
    insert_Features(4, 'Cadillac Mountain-Jordan Pond-Somes Sound', 'visitor center-bathrooms-gift shop-lighthouse', 'Oak-Birch-Choke Cherry', 'Squirell-Deer-Raccoon')
    insert_Features(5, 'Colorado River-South Rim-North Rim', 'visitor centers-bathrooms-gift shops', 'Engleman Spruce-Douglas Fir-Aspen-Mountain Ash', 'Bighornn Sheep-Wild Burros-Coyote-Salamander-Trout-Walleye-Catfish')
    insert_Features(6, 'Kelso Dunes-Clark Mountains-lava flows-lava domes', 'visitor center-bathrooms-gift shops-train station', 'Joshua Tree-Cresote bush-Pinion Juniper-Yucca', 'Tortise-Badger-Coyote')
    insert_Features(7, 'Devils Postpile-Rainbow Falls', 'visitor center-bathrooms-gift shop', 'Lodgepole Pine-White Fir-Red Fir-Willows-Black Cottonwood', 'Black Bear-Pine Marten-Mule Deer')
    insert_Features(8, 'San Andreas Fault-Pacific Ocean-Sand Dunes-Wetlands-Marshes', 'visitor center-bathrooms-gift shop-light house', 'Sky Lupine-California Poppies-Bull Kelp', 'Harbor Seal-Bobcat-Coyote-Elephant Seal-Elk-Califonia Grey Whale')
    insert_Features(9, 'prarie-grassland-ephemeral marshes-ponds', 'visitor center-bathrooms-gift shop', 'Giant Bristle Grass-Sargassum Weed-Roughseed Sea Purslane', 'Ghost Crab-Sheepshead-Redfish-Flounder-Black Drum-Coyote-Deer-Leatherback Sea Turtle-Green Sea Turtle-Kemps Ridley Sea Turtle-Loggerhead Sea Turtle-Hawksbill Sea Turtle')
    insert_Features(10, 'San Diego Harbor-North Island-', 'lighthouse-visitor center-bathrooms-gift shop', 'snake cholla-prickly pear cactus-Mojave yucca-Shaws agave-California coast poppy-Indian paintbrush-California buckwheat-California sagebrush-lemonadeberry', 'Grey Whale-Trapdoor Spider-Great Blue Heron-California Quail-Canyon Bat')
    insert_Features(11, 'mixed grass prarie-sandstones-siltstones-mudstones-claystones-limestones-volcanic ash', 'visitorcenters-bathroom-overlooks', 'Western Wheatgrass-juniper', 'Bison-Pronghorn-Prarie Dog-Rattlesnake')
    insert_Features(12, 'Continental Divide-Glaciers-Mount Ida-McHenrys Peak', 'visitorcenters-bathrooms-boat launch', 'Lichen-Liverwort-Moss-Aspen-Columbine', 'Moose-Bighorn Sheep-Elk-Black Bear-Coyote-Mule Deer-Cougar')
    insert_Features(13, 'Temperate Rainforest-Hoh River-Hall of Mosses Trail-Elwah River-Glaciers-Rialto Beach', 'visitorcenters-bathrooms-boat launch-overlooks', 'Big Leaf Maples-Sitka Spruce-Western Hemlock', 'Mountain Goat-Cougar-Bald Eagle-Black Bear-Elk-Harbor Seal')
    insert_Features(14, 'Star Dune-Mendano Creek-Sangre De Christo Mountains-High Dune', 'visitorcenter-bathrooms', 'Ponderosa Pine-Pinion Juniper-Cottonwood-Aspen-Red Osier Dogwood-Bristlecone Pine-Limber Pine', 'Pika-Ptarmigan-Marmot-Bighorn Sheep-Cougar-Mule Deer-Owl-Dusky Grouse-Turkey-Elk-Pronghorn')
    insert_Features(15, 'Appalacian Trail-Clingmans Dome-Newfound Gap-Cades Cove-Chimney Tops-Andrews Bald', 'visitorcenter-bathrooms', 'Dogwood-Azalea-Sweet Birch-Eastern White Pine-Eastern Red Bud', 'Black Bear-Spotfin Chub-salamanders-River Otter-Elk-Peregrine Falcon-Northern Flying Squirrel')

    print("success")
    print("++++++++++++++++++++++++++++++++++")

def insert_Location(_conn, _parkID, _state, _address, _county, _city, _zipcode):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert Location")

    try:
           sql = """INSERT INTO Location(parkIDNumber, state, address, county, city, zipcode)
               VALUES(?, ?, ?, ?, ?, ?)"""
           args = [_conn, _parkID, _state, _address, _county, _city, _zipcode]
           _conn.execute(sql, args)
           _conn.commit()
           print("successs")
    except Error as e:
           _conn.rollback()
           print(e)
    print("++++++++++++++++++++++++++++++++++")

def populateTable_Location (_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Location")
    insert_Location(21, 'Maryland-Virginia', '7206 Naional Seashore Ln-8586 Beach Rd', 'Worcester-Accomack', 'Berlin-Chincoteague', 21811)
    insert_Location(20, 'Massachusetts', '50 Nauset Rd', 'Barnstable', 'Eastham', 2642)
    insert_Location(19, 'Utah', 'Forbidding Canyon Lake', 'San Juan', 'Powell', 84533)
    insert_Location(18, 'Oregon', '32651 Highway 19', 'Wheeler-Grant', 'Kimberly', 97848)
    insert_Location(17, 'New York', 'Liberty Island', 'New York', 'New York', 10004)
    insert_Location(16, 'Virginia', '21073 Skyline Dr', 'Warren', 'Front Royal', 22630)
    insert_Location(15, 'Tennessee', '107 Park Headquarters Rd', 'Sevier', 'Gatlinburg', 37738)
    insert_Location(14, 'Colorado', 'Visitor Center 11999 State Highway 150', 'Saguache-Alamosa', 'Mosca', 81146)
    insert_Location(13, 'Washington', '3002 Mt Angeles Rd', 'Jefferson', 'Port Angeles', 98362)
    insert_Location(12, 'Colorado', '1000 US Hwy 36', 'Larimer', 'Estes Park', 80517)
    insert_Location(11, 'South Dakota', '25216 Ben Reifel Rd', 'Oglala Lakota', 'Interior', 57750)
    insert_Location(10, 'California', '1800 Cabrillo Memorial Dr', 'San Diego', 'San Diego', 92106)
    insert_Location(9, 'Texas', '20420 Park Rd 22', 'Kleberg', 'Corpus Christi', 92106)
    insert_Location(8, 'California', '1 Bear Valley Rd', 'Marin', 'Point Reyes Station', 94956)
    insert_Location(7, 'California', 'Devils Postpile Rd', 'Madera', 'Mammoth Lakes', 93546)
    insert_Location(6, 'California', '90942 Kelso Cima Rd', 'San Bernardino', 'Essex', 92332)
    insert_Location(5, 'Arizona', '20 South Entrance Rd', 'Mohave', 'Grand Canyon', 86023)
    insert_Location(4, 'Maine', '25 Visitor Center Rd', 'Hancock-Knox', 'Bar Harbor', 4609)
    insert_Location(3, 'Utah', 'Arches National Park Rd', 'Grand', 'Moab', 84532)
    insert_Location(1, 'Montana-Wyoming', 'North Entrance Rd-2 Officers Row', 'Teton-Gallatin', 'Gardiner-Cody', 59030-82190)
    
    print("success")
    print("++++++++++++++++++++++++++++++++++")

def insert_Permit(_conn, _parkId, _idNumber, _ownerName, _type, _duration, _startDate, _endDate):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert Permit")

    try:
           sql = """INSERT INTO Permits(parkIdNumber, IdNumber, ownerName, type, duration, startDate, end-date)
               VALUES(?, ?, ?, ?, ?, ?, ?)"""
           args = [_parkId, _idNumber, _ownerName, _type, _duration, _startDate, _endDate]
           _conn.execute(sql, args)
           _conn.commit()
           print("successs")
    except Error as e:
           _conn.rollback()
           print(e)
    print("++++++++++++++++++++++++++++++++++")

def populateTable_Permits (_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Permits")
    insert_Permit(2, 1, 'Royal Robbins', 'rockclimbing', 30, '2023-07-01', '2023-08-01')
    insert_Permit(2, 2, 'John Long', 'rockclimbing', 30, '2023-07-01', '2023-08-01')
    insert_Permit(2, 3, 'John Bachar', 'rockclimbing', 30, '2023-07-01', '2023-08-01')
    insert_Permit(2, 4, 'Warren Harding', 'rockclimbing', 30, '2023-07-01', '2023-08-01')
    insert_Permit(11, 1, 'Mike Piazza', 'camping', 3, '2024-05-01', '2024-05-04')
    insert_Permit(14, 1, 'Thomas Redbook', 'hiking', 1, '2023-10-31', '2023-10-31')
    insert_Permit(2, 5, 'Scrooge McDuck', 'camping', 2, '2023-12-30', '2023-12-31')
    insert_Permit(2, 6, 'Baloo', 'camping', 3, '2023-11-17', '2023-11-20')
    insert_Permit(2, 7, 'Chip', 'camping', 4, '2023-11-1', '2023-11-5')
    insert_Permit(5, 5, 'Jim Peterson', 'backpacking', 6, '2023-11-1', '2023-11-5')
    insert_Permit(12, 1, 'Thomas Finley', 'backpacking', 3, '2023-09-12', '2023-09-15')
    insert_Permit(14, 1, 'Agustine Burnhard', 'backpacking', 12, '2023-10-11', '2023-10-23')
    insert_Permit(16, 1, 'Jim Lee', 'backpacking', 5, '2023-07-11', '2023-07-16')
    insert_Permit(1, 1, 'Albert Einstein', 'backpacking', 13, '2023-07-01', '2023-07-14')
    insert_Permit(1, 2, 'Henry Ford', 'camping', 4, '2023-08-04', '2023-08-4')

    print("success")
    print("++++++++++++++++++++++++++++++++++")

def insert_Recreation(_conn, _parkID, _permitID, _activity, _trailName, _trailHead, _road, _campsiteName):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert Recreation")

    try:
           sql = """INSERT INTO Recreation(parkIDNumber, permitIDNumber, activity, trailName, trailHead, road, campsiteName)
               VALUES(?, ?, ?, ?, ?, ?, ?)"""
           args = [_parkID, _permitID, _activity, _trailName, _trailHead, _road, _campsiteName]
           _conn.execute(sql, args)
           _conn.commit()
           print("successs")
    except Error as e:
           _conn.rollback()
           print(e)
    print("++++++++++++++++++++++++++++++++++")

def populateTable_Recreation (_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Recreation")
    insert_Recreation(1, 1, 'backpacking', 'Dawson', 'Rose', ' ',' ')
    insert_Recreation(2, 1, 'rockclimbing', '-', '-', '-','Camp 4')
    insert_Recreation(2, 2, 'rockclimbing', '-', '-', '-','Camp 4')
    insert_Recreation(2, 3, 'rockclimbing', '-', '-', '-','Camp 4')
    insert_Recreation(2, 4, 'rockclimbing', '-', '-', '-','Camp 4')
    insert_Recreation(14, 1, 'hiking', 'Dune Trail', 'Dune', 'Castle Creek','-')
    insert_Recreation(11, 1, 'camping', '-', '-', 'Park Rd','Cochise')

    
    print("success")
    print("++++++++++++++++++++++++++++++++++")

def insert_Staff(_conn, _employeeId, _parkId, _department, _schedule, _name):
    print("++++++++++++++++++++++++++++++++++")
    print("Insert Staff")

    try:
           sql = """INSERT INTO Staff(employeeIDNumber, parkIDNumber, department, schedule, name)
               VALUES(?, ?, ?, ?, ?)"""
           args = [_employeeId, _parkId, _department, _schedule, _name]
           _conn.execute(sql, args)
           _conn.commit()
           print("successs")
    except Error as e:
           _conn.rollback()
           print(e)
    print("++++++++++++++++++++++++++++++++++")

def populateTable_Staff (_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Staff")
    insert_Staff(1, 1, 'JANITORIAL', 'M__T_SS', 'Richard Sheryl')
    insert_Staff(2, 3, 'RANGER', 'MTWT__S', 'Sherry Woods')
    insert_Staff(3, 5, 'FIRE_DEPARTMENT', 'MT___SS', 'Michael Osborn')
    insert_Staff(4, 7, 'FIRE_DEPARTMENT', 'MTWTFSS', 'Louie Von Hatter')
    insert_Staff(5, 9, 'JANITORIAL', '__WTFS_', 'Richard Doberman')
    insert_Staff(6, 10, 'VISITOR_CENTER', 'M__TFSS', 'Carlson Ford')
    insert_Staff(7, 3, 'INTERNAL_AFFAIRS', 'MTW_FSS', 'Harrison Shepherd')
    insert_Staff(8, 6, 'RANGER', 'MTWT__S', 'Alex Benjamin')
    insert_Staff(9, 12, 'JANITORIAL', 'MT_TF_S', 'Cherry Groveson')
    insert_Staff(10, 14, 'FIRE_DEPARTMENT', '___TF_S', 'Adam Sandson')
    insert_Staff(11, 1, 'RANGER', 'M_WT__S', 'Leo Skywalker')
    insert_Staff(12, 3, 'INTERNAL_AFFAIRS', 'M__T_SS', 'Timothy Stockson')
    insert_Staff(13, 9, 'VISITOR_CENTER', '__WTFSS', 'Grover Berry')
    insert_Staff(14, 21, 'RANGER', 'MT___SS', 'Adam Sandson')
    insert_Staff(15, 18, 'JANITORIAL', 'M_WTFSS', 'Roger Cameron')
    insert_Staff(16, 15, 'MANAGEMENT', 'MTW_F__', 'Rico Diesel')
    insert_Staff(17, 17, 'MANAGEMENT', 'MT__FSS', 'Alexis Sheema')
    insert_Staff(18, 17, 'JANITORIAL', 'MT_TFSS', 'Harry Porter')

    print("success")
    print("++++++++++++++++++++++++++++++++++")

def populateTables(_conn):
    populateTable_Park(_conn)
    populateTable_Fees(_conn)
    populateTable_Recreation(_conn)
    populateTable_Staff(_conn)
    populateTable_Permits(_conn)
    populateTable_Features(_conn)


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
        l = '{:>10} {:>10} {:>10} {:>10} {:>10}'.format("Name", "Designation", "Address", "City", "Zip Code")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10} {:>10} {:>10} {:>10}'.format(row[0], row[1], row[2], row[3], row[4])
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

def featureByPark(_conn, _park):
    print("++++++++++++++++++++++++++++++++++")

    print("Features in: ", _park, " park.")

    try:
        sql = """SELECT Park.name, Features.featureName
                    FROM Features, Park
                    WHERE Features.parkIDNUMBER = Park.IdNumber
                    AND Park.name = ?"""
        args = [_park]

        cur = _conn.cursor()
        cur.execute(sql, args)

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

def expsActivities(_conn):
    print("++++++++++++++++++++++++++++++++++")

    print("Most expensive Acitivty from every Park.")

    try:
        sql = """SELECT Fees.permitType, Park.name, Fees.amount
                    FROM Park, Fees
                    WHERE Park.IdNumber = Fees.parkIDNumber

                    INTERSECT 
                        
                    SELECT Fees.permitType, Park.name, MAX(Fees.amount)
                    FROM Park, Fees
                    WHERE Fees.parkIDNumber = Park.iDNumber
                    GROUP BY Park.iDNumber"""

        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10} {:>10} {:>10}'.format("Permit", "Park", "Fee")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10} {:>10}'.format(row[0], row[1], row[2])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def prkPermitbyStMonth(_conn, _sdate):
     print("++++++++++++++++++++++++++++++++++")
     
     print("Park, permit owner starting on ", _sdate)
     
     try:
         sql = """SELECT Park.name, Permits.ownerName, Permits.type
                    FROM Park, Permits
                    WHERE Park.iDNumber = Permits.parkIDNumber
                    AND Permits.startDate LIKE ?"""
         
         args = [_sdate]
         
         cur = _conn.cursor()
         cur.execute(sql, args)

         l = '{:>10} {:>10} {:>10}'.format("Park", "Permit Holder", "Permit Type")
         print(l)
         print("-------------------------------")

         rows = cur.fetchall()
         for row in rows:
            l = '{:>10} {:>10} {:>10}'.format(row[0], row[1], row[2])
            print(l)


     except Error as e:  
        print(e)

     print("++++++++++++++++++++++++++++++++++")

def staffAtPrk(_conn):
    print("++++++++++++++++++++++++++++++++++")
    
    print("Staff at each park.")

    try:
        sql= """SELECT Park.name, Staff.name
                    FROM Park, Staff
                    WHERE Park.iDNumber = Staff.parkIDNumber"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        l = '{:>10} {:>10}'.format("Park", "Employee")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0], row[1])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def permitFeeperPark(_conn, _park, _act):
    print("++++++++++++++++++++++++++++++++++")

    print("Fee amount for ", _act, " at ", _park)

    try:
        sql = """SELECT Fees.amount, Fees.permitType, Park.name
                    FROM Park, Fees
                    WHERE Park.iDNumber = Fees.parkIDNumber
                    AND Fees.permitType = ?
                    AND Park.name = ? """
        
        args = [_act, _park]

        cur = _conn.cursor()
        cur.execute(sql, args)

        l = '{:>10} {:>10} {:>10}'.format("Fee", "Permit Type", "Park")
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

    print(_park, " hours: ")

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

def listTrails(_conn, _park):
    print("++++++++++++++++++++++++++++++++++")

    print("List of Trails from ", _park)

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

def totPermitsperPark(_conn, _park):
    print("++++++++++++++++++++++++++++++++++")

    print("Max permit number and number of permits for ",_park)

    try:
        sql = """SELECT Park.totalNumPermits, Count(Permits.IdNumber), Park.name
                    FROM Park, Permits
                    WHERE Park.iDNumber = Permits.parkIDNumber
                    AND Park.name = ?"""

        args = [_park]
        cur = _conn.cursor()
        cur.execute(sql, args)

        l = '{:>10} {:>10} {:>10}'.format("Total allowed Permits", "Number of Permits", "Park")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10} {:>10}'.format(row[0], row[1], row[2])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def permitsbyPark(_conn):
    print("++++++++++++++++++++++++++++++++++")

    print("All permits in each park")

    try:
        sql = """SELECT Park.name, Permits.type, Permits.ownerName
                    FROM Permits, Park
                    WHERE Park.iDNumber = Permits.parkIDNumber"""
        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10} {:>10} {:>10}'.format("Park", "Permit type", "Permit Owner")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10} {:>10}'.format(row[0], row[1], row[2])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def featuresByState(_conn):
    print("++++++++++++++++++++++++++++++++++")

    try: 
        sql = """SELECT L.state,F.fauna, F.flora, F.featureName
                    FROM Features F, Location L
                    WHERE F.parkIdNumber = L.parkIdNumber"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        
        l = '{:>10} {:>10} {:>10} {:>10}'.format("State", "Animals", "Plants", "Features")
        print(l)
        print("-------------------------------")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10} {:>10} {:>10}'.format(row[0], row[1], row[2], row[3])
            print(l)
    
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def totalFeesbyPark(_conn):
    print("++++++++++++++++++++++++++++++++++")

    try:
        sql = """SELECT Sum(F.amount), Park.name
                    FROM Fees F, Park
                    WHERE F.permitType IN (   
                        SELECT P.type
                        FROM Park, Permits P
                        WHERE Park.IdNumber = P.parkIdNumber)
                    AND Park.iDNumber = F.parkIdNumber
                    GROUP BY F.parkIdNumber"""
        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10} {:>10}'.format("Total Fees", "Park")
        print(l)
        print("-------------------------------")     

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0], row[1])
            print(l)

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def stateStDatebyPerson(_conn):
    print("++++++++++++++++++++++++++++++++++")

    try: 
        sql = """SELECT l.state, p.startDate
                    FROM Location l, Fees f, Permits p
                    WHERE l.parkIDNumber = f.parkIDNumber
                    AND f.permitType = p.type
                    AND p.ownerName = "John Long";"""
        
        cur = _conn.cursor()
        cur.execute(sql)

        l = '{:>10} {:>10}'.format("State", "Start Date")
        print(l)
        print("-------------------------------")  
        
        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0], row[1])
            print(l)

    except Error as e:
        print(e)    

    print("++++++++++++++++++++++++++++++++++")


def main():
    database = r"project.db"

    # create a database connection
    conn = openConnection(database)
    #dropTables(conn)
    #createTables(conn)
    #populateTables(conn)
    parksAllowSwimming(conn)            #1
    cmpPermitsFees(conn)                #2
    parksHvBearsCamping(conn)           #3
    actInShenandoah(conn)               #4
    typesOfPark(conn)                   #5
    countStaff(conn)                    #6
    featureByPark(conn, "Yellowstone")  #7
    expsActivities(conn)                #8
    prkPermitbyStMonth(conn, "2023-11-1") #9      #change function name?
    staffAtPrk(conn)                    #10
    permitFeeperPark(conn, "Yosemite", "backpacking")   #11
    parkOprHrs(conn, "Great Smokey Mountains")          #12
    listTrails(conn, "Great Sand Dunes")                #13
    totPermitsperPark(conn, "Yosemite")                 #14
    permitsbyPark(conn)                                #15
    featuresByState(conn)                              #16
    totalFeesbyPark(conn)                              #17
    stateStDatebyPerson(conn)


    closeConnection(conn, database)


if __name__ == '__main__':
    main()
