userArray = [['houghs','hello1234'],['merkink','boffnegg'],['lovegrovec','conall']]

def Login():
    global userArray
    usernameI = input("Enter Username: \n")
    passwordI = input("Enter Password: \n")

    correct = False
    for user in userArray:
        if usernameI == user[0] and passwordI == user[1]:
            match = True
            break

    if match == True:
        print("Access granted.")
    else:
        print("Access denied.")

def Signup():
    global userArray
    newUser = input("Enter NEW Username: \n")

    user_exists = False
    #print("Help Me")
    #print("Lol nah")
    #print("K")
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
        print("Error the username already exists.")
        signup()

def menu():
    selectMenu = int(input("Select: \n 1. Login \n 2. Signup \n")

    if selectMenu == "1":
        Login()

    elif selectMenu == "2":
        Signup()

    else:
        print("Invalid input.")
        menu()

menu()