from queries import printAllParks, openConnection, closeConnection, printAllRecreation, parkFeatures, printParkFee, allParkActivities, parkOprHrs, listTrails, permitsByPark, featuresByPark, featuresByState, structByPark, stateDatebyPerson, totalFeesbyPark, staffByState
from queries import createPermit
def menu(_conn):
    print("==== Main Menu ====")
    print("(0) Quit Program")
    print("(1) Select Park Menu")  
    print("(2) Select Features Menu")
    print("(3) Select Recreation Menu")
    print("(4) Select Administrative Menu")
    res = -1
    while(res != 0 or res > 3):
        check = input("Enter number: ")
        
        if check.isdigit():
            res = int(check)
        else:
            print("Please enter a number.")

        if res == 1:
            sub_menu_Parks(_conn)
        elif res == 2: 
            sub_menu_Features(_conn)
        elif res == 3:
            sub_menu_Recreation(_conn)
        elif res == 4:
            sub_menu_Admin(_conn)

        print("==== Main Menu ====")
        print("(0) Quit Program")
        print("(1) Select Park Menu")   
        print("(2) Select Features Menu")
        print("(3) Select Recreation Menu")
        print("(4) Select Administrative Menu")

def sub_menu_Parks(_conn):

    print("==== Parks Sub-Menu ====")
    print("(0) Quit sub menu")
    print("(1) List all Parks")
    print("(2) List all Features in Selected Park")
    print("(3) List all Allowed activities in Selected Park")
    print("(4) List Fee for selected activity in Selected Park")
    print("(5) List Operating Hours for Selected Park")
    res = -1
    while (res != 0):
        check = input("Enter number: ")

        if check.isdigit():
            res = int(check)
        else:
            print("Please enter a number.")

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
    print("==== Recreation Sub-Menu ====")
    print("(0) Quit sub menu")
    print("(1) List all Activities")
    print("(2) List all Trails in Selected Park")
    print("(3) List all Permits in Selected Park")
    print("(4) List Structures in Selected Park") 
    res = -1
    while (res != 0):
        check = input("Enter number: ")
        
        if check.isdigit():
            res = int(check)
        else:
            print("Please enter a number.")

        if res == 1:
            printAllRecreation(_conn)
            res = 0
        elif res == 2:
            _park = input("Enter park name: ")
            listTrails(_conn, _park)
            res = 0
        elif res == 3:
            _park = input("Enter park name: ")
            permitsByPark(_conn, _park)
            res = 0
        elif res == 4:
            _park = input("Enter park name: ")
            structByPark(_conn, _park)
            res = 0
        

def sub_menu_Features(_conn):
    print("==== Features sub menu ====")
    print("(0) Quit sub menu")
    print("(1) List all Features of Selected Park")
    print("(2) List all Features by Selected State")
    print("(3) List all Permits in Selected Park") # edit
    print("(4) List Fee for selected activity in Selected Park") #edit
    res = -1
    while (res != 0):
        check = input("Enter number: ")
        
        if check.isdigit():
            res = int(check)
        else:
            print("Please enter a number.")

        if res == 1:
            _park = input("Enter park name: ")
            featuresByPark(_conn, _park)
            res = 0
        elif res == 2:
            _state = input("Enter state name: ")
            featuresByState(_conn, _state)
            res = 0
        elif res == 3:
            _park = input("Enter park name: ")
            permitsByPark(_conn, _park)
            res = 0

def sub_menu_Admin(_conn):
    print("==== Administrative sub menu ====")
    print("(0) Quit sub menu")
    print("(1) List State, & Start date of Permit Owner")
    print("(2) List Total Fees from Selected Park")
    print("(3) List Staffing at Parks by Selected State")
    print("(4) Create Permit")

    res = -1
    while (res != 0):
        check = input("Enter number: ")
        
        if check.isdigit():
            res = int(check)
        else:
            print("Please enter a number.")

        if res == 1:
            _name = input("Enter permit owner name: ")
            stateDatebyPerson(_conn, _name)
            res = 0
        
        elif res == 2:
            _park = input("Enter park name: ")
            totalFeesbyPark(_conn, _park)
            res = 0
        
        elif res == 3:
            _state = input("Enter state name: ")
            staffByState(_conn, _state)
            res = 0
        elif res == 4:
            gate = 0
            while gate != 1:
                _name = input("Enter permit owner name: ")
                _act = input("Enter permit type: ")
                _park = input("Enter park name: ")
                _sdate = input("Enter start date YYYY-MM-DD: ")
                _edate = input("Enter end date YYYY-MM-DD: ")
                _dur = input("Enter duration: ")
                if _dur.isdigit():
                    gate = 1
                else:
                    print("You must enter a number for the duration!")
            
            createPermit(_conn, _park, _name, _act, _sdate, _edate, _dur)
            res = 0

def main():
    database = r"db.sqlite"
    conn = openConnection(database)
    menu(conn)
    closeConnection(conn, database)

if __name__ == '__main__':
    main()