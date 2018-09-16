userArray = [['houghs','hello1234'],['merkink','boffnegg'],['lovegrovec','conall']]

def Login():
    global userArray
    usernameI = input("Enter Username: \n")
    passwordI = input("Enter Password: \n")

    match = False
    for user in userArray:
        if usernameI == user[0] and passwordI == user[1]:
            match = True
            break

    if match == True:
        print("Access granted.")
    else:
        print("Access denied.")
        menu()

def Signup():
    global userArray
    newUser = input("Enter NEW Username: \n")

    user_exists = False
    for user in userArray:
        if user[0] == newUser:
            user_exists = True

    if user_exists == False:
        newPass = input("Enter NEW Password: \n")
        newLogin = [newUser, newPass]
        userArray.append(newLogin)
        print("New User Added.")
        menu()
    else:
        user_exists = True
        print("Error the username already exists.")
        Signup()

def menu():
    menuSelect = input("Select menu option:\n\
1. Login\n\
2. Signup\n")
    if menuSelect == "1":
        Login()
    if menuSelect == "2":
        Signup()
    else:
        menu()

menu()