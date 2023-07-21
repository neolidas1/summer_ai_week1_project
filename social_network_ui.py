# You can implement user interface functions here.

def mainMenu():
    print("")
    print("1. Create a new account")
    print("2. Manage my account")
    print("3. Quit")
    print("********************************************************")
    return input("Please Choose a number: ")

def manageAccountMenu():
    print("")
    print("1. Edit my details")
    print("2. Add a friend")
    print("3. View all my friends")
    print("4. View all my messages")
    print("5. Block a friend.")
    print("6. <- Go back ")
    return input("Please Choose a number: ")

def editDetails():
    editName = input("Enter your new name: ")
    editAge = input("Enter your new age: ")
    editBio = input("What is your favorite animal? Favorite movie? Favorite book? Put down anything interesting about yourself down here! ")
    return editName, editAge, editBio 

def editName():
    print("")
    return input("Enter your new name: ")

def editAge():
    print("")
    return input("Enter your new age: ")

def editBio():
    print("")
    return input("Enter interesting facts! ")

def addFriend():
    print("")
    return input("Please enter your friend's name")
