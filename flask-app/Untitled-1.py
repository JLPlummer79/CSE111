from queries import printAllParks, openConnection, closeConnection, printAllRecreation, parkFeatures, printParkFee, allParkActivities, parkOprHrs, listTrails, permitsByPark

def menu(_conn):
    print("(0) Quit Program")
    print("(1) Select Park Menu")   #sub-menu for park queries
    print("(2) to see all Features")# will bec sub menu for 
    print("(3) to view Recreation")
    res = -1
    while(res != 0 or res > 3):
        res = int(input("Enter number: "))

        if res == 1:
            sub_menu_Parks(_conn)
        elif res == 2: 
            #query all features
            print("query all features")
        elif res == 3:
            print("query all recreation activities")
            sub_menu_Recreation(_conn)
            #printAllRecreation(_conn)


        print("(0) Quit Program")
        print("(1) Select Park Menu")   #will turn into a sub-menu for park queries
        print("(2) to see all Features")# will bec sub menu for 
        print("(3) Select Recreation Menu")

def sub_menu_Parks(_conn):
    print("(0) Quit sub menu")
    print("(1) List all Parks")
    print("(2) List all Features in Selected Park")
    print("(3) List all Allowed activities in Selected Park")
    print("(4) List Fee for selected activity in Selected Park")
    print("(5) List Operating Hours for Selected Park")
    res = -1
    while (res != 0):
        res = int(input("Enter number:"))
        if res == 1:
            printAllParks(_conn)
            res = 0
        elif res == 2:
            park = input("Enter park name: ")
            parkFeatures(_conn,park)
            res = 0
        elif res == 3:
            park = input("Enter park name: ")
            allParkActivities(_conn, park)
            res = 0
        elif res == 4:
            _park = input("Enter park name: ")
            _act = input("Enter activity: ")
            printParkFee(_conn, _act, _park)
            res = 0
        elif res == 5:
            _park = input("Enter park name: ")
            parkOprHrs(_conn, _park)
            res = 0

def sub_menu_Recreation(_conn):
    print("(0) Quit sub menu")
    print("(1) List all Parks")
    print("(2) List all Trails in Selected Park")
    print("(3) List all Permits in Selected Park")
    print("(4) List Fee for selected activity in Selected Park")
    res = -1
    while (res != 0):
        res = int(input("Enter number: "))
        if res == 1:
            printAllParks(_conn)
            res = 0
        elif res == 2:
            _park = input("Enter park name: ")
            listTrails(_conn, _park)
            res = 0
        elif res == 3:
            _park = input("Enter park name: ")
            permitsByPark(_conn, _park)
            res = 0
            

def main():
    database = r"db.sqlite"
    conn = openConnection(database)
    menu(conn)
    closeConnection(conn, database)

if __name__ == '__main__':
    main()