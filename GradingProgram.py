'''
Grade Program



'''

ValidUserList = [['chrisf','wizard'],['alexf','cat']]
Students = {
    'Alex':[92,76,88]
    }

def logon(UserList):
    authenticated = 0
    while authenticated == 0:
        user = input("Username: ")
        password = input("Password: ")
        for checkCred in ValidUserList:
            if checkCred[0] == user and checkCred[1] == password:
                authenticated = 1
        if authenticated == 0:
            print("Invalid creditials.\n")
        else:
            print("Welcome",user)
        

def mainMenu():
    selection = 0
    while selection == 0:
        print("Welcome to Grade Central\n")
        print("[1] - Enter Grades")
        print("[2] - Remove Student")
        print("[3] - Student Average Grades")
        print("[4] - Exit\n")
        selection = input("What would you like to do today? (Enter a Number): ")
        if int(selection) < 1 or int(selection) > 4:
            selection = 0
            print("Invalid Option Selected\n")
    return int(selection)
            

# Main Program

#logon(ValidUserList)
selection = 0
while selection != 4:
    selection = mainMenu()
    if selection == 1:
        print("Enter Grades")
    if selection == 2:
        print("Remove Student")
    if selection == 3:
        print("Student Average Grades")

print("Done")
