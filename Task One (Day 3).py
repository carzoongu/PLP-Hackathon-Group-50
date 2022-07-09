#Date time module
import datetime
from datetime import datetime
date = datetime.today()

#Set the password
set_password = input("Set your password: ")
correct_password = set_password

#Let the user have three attempts to enter the password
password_count = 0
password_limit = 3
while password_count < password_limit:
    password = input("Enter your password: ")
    password_count +=1
    if password == correct_password:
        print("Correct Password! Acess Granted")
        break
    else:
        print("Wrong Password! Try Again")
else:
    print("You Entered Incorrect password Three times")
        
#Executing the commands        
commands = ""
opened = False

while True:
    commands = input("Enter your action> ")
    if commands.lower() == "open":
        if opened:
            print("The door is already open")
            print("The door was last open at ",date)
        else:
            opened = True
            print("The door is now open")
            print("The door was last open at ",date)
    elif commands.lower() == "close":
        if not opened:
            print("The door is already closed")
            print("The door was last opened at ",date)
        else:
            opened = False
            print("The door is now closed")
            print("The door was last opened at ",date)
    elif commands.lower() == "quit":
        break
    else: