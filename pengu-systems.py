import subprocess
import sys
import os
import bcrypt
from getpass import getpass
import random

# Function to create and activate a virtual environment
def setup_virtual_environment():
    venv_name = "PenguSystems"
    # Check if the virtual environment already exists
    if not os.path.exists(venv_name):
        print(f"Creating virtual environment: {venv_name}")
        subprocess.check_call([sys.executable, "-m", "venv", venv_name])
        print("Installing required packages...")
        subprocess.check_call([os.path.join(venv_name, "bin", "pip"), "install", "bcrypt"])
        print("Creating user_data.txt file...")
        with open("user_data.txt", "w") as f:
            f.write("username,password\n")
    else:
        print(f"Activating virtual environment: {venv_name}")
    
    # Activate the virtual environment
    if os.name == 'nt':
        activate_script = os.path.join(venv_name, "Scripts", "activate.bat")
        subprocess.call(activate_script, shell=True)
    else:
        activate_script = os.path.join(venv_name, "bin", "activate")
        subprocess.call(f"source {activate_script}", shell=True)

# Call the setup function
setup_virtual_environment()

###########################################################################################

version = 2.01

###########################################################################################

print(f"version: {version}")
print("")

###########################################################################################

class usr:
    def __init__(self, name, pw) -> None:
        self.name = name
        # Check if the password is already hashed (bcrypt hashes are typically 60 characters long)
        if len(pw) == 60:
            self.pw = pw
        else:
            self.pw = self._hash_password(pw)

    @staticmethod
    def _hash_password(password):
        password_bytes = password.encode('utf-8')
        hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        return hashed.decode('utf-8')
    
user_list = []

class expensive_objects:
    def __init__(self, object_name, object_price) -> None:
        self.name = object_name
        self.price = object_price
    def __str__(self) -> str:
        return f"{self.name}"
expensive_objects_list = []
expensive_object = expensive_objects('Wallet on Chain Ivy 👝 - Luis Vuitton (purse)', 1850)
expensive_objects_list.append(expensive_object)

###########################################################################################

# hash_password-check

def hash_password(pw): 
    password_bytes = pw.encode('utf-8') 
    hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt()) 
    return hashed.decode('utf-8')

# load_users

def load_users():
    with open("user_data.txt", "r") as f:
        next(f)  # Skip header line
        for line in f:
            name, pw = line.strip().split(",")
            user_list.append(usr(name, pw))

# save_user

def save_user(user):
    print(f"Saving user: {user.name}, Password: {user.pw}")
    with open("user_data.txt", "a") as f:
        f.write(f"{user.name},{user.pw}\n")
    print("User saved successfully")
    verify_data()

# Verify Data

def verify_data():
    with open("user_data.txt", "r") as f:
        next(f)  # Skip header line
        print("Verifying data in the file:")
        for line in f:
            print(line.strip())

# user_list

def users_list():
    print("Existing usernames:")
    for user in user_list:
        print(user.name)

# login_or_signup

def login_or_signup():
    load_users()
    while True:
        print("Do you want to login or signup?")
        answer = input("-> ")
        if answer in ["login", "log in", "lg"]:
            os.system('cls' if os.name == 'nt' else 'clear')
            usrname = input("Enter your username: ")
            if not any(user.name == usrname for user in user_list):
                os.system('cls' if os.name == 'nt' else 'clear')
                print("This username does not exist, you will be sent back to the login process. 🔒")
                login_or_signup()
            pw = getpass("Enter your password: ")
            if any(user.name == usrname and bcrypt.checkpw(pw.encode('utf-8'), user.pw.encode('utf-8')) for user in user_list):
                print("")
                print(f"Welcome on board {usrname}! 🚢")
                what_do_you_want_to_do()
                return
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("This password is incorrect, you will be sent back to the login process. 🔒")
                login_or_signup()
                break
        elif answer in ["signup", "sign up", "sp"]:
            usrname = input("Enter your new username: ")
            pw = getpass("Enter your new password: ")
            hashed_pw = hash_password(pw)
            new_user = usr(usrname, hashed_pw)
            user_list.append(new_user)
            save_user(new_user)
            print("")
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Welcome on board {usrname}! 🚢")
            what_do_you_want_to_do()
            return
        elif answer in ["userlist",  "ulist", "ul", "user list"]:
            print("")
            users_list()
            print("")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("-> Sorry pls answer with login or signup, thank you. 🤗")

# what_do_you_want_to_do

def what_do_you_want_to_do():
    ok = False
    while ok == False:
        print("What do you want to do?")
        print("-> you can [logout] or play [priceguesser]")
        answer = input("-> ")
        if answer in ["logout", "log out", "lg"]:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("You've been locked out of the system 🔑")
            print("")
            ok = True
            login_or_signup()
            os.system('cls' if os.name == 'nt' else 'clear')
        elif answer in ["priceguesser", "price guesser", "guesse the price", "pg"]:
            ok = True
            priceguesser()
            os.system('cls' if os.name == 'nt' else 'clear')
        elif answer in ["exit", "EXIT", "Exit"]:
            ok = True
            os.system('cls' if os.name == 'nt' else 'clear')
            exit()
        else:
            print(" -> Sorry pls answer with logout or priceguesser, thank you. 🤗")

# priceguesser

def priceguesser():
    guessed = 0
    maxattempts = 5
    list_length = len(expensive_objects_list)
    print("")
    print("Welcome to PriceGuesser! 💰")
    print("Now you can guess the price of very expensive objects! 💸")
    print("")
    print("Ok let's start with the first very expensive object, the first expensive")
    object_number = random.randint(0, list_length - 1)
    object = expensive_objects_list[object_number]
    print(f"object is a {object}.")
    print("")
    print(f"How expensive is this object? You have {maxattempts} attempts to guess the price.")
    while guessed < maxattempts:
        guessed += 1
        print(f"-> Attempt: {guessed}")
        estimated_price = int(input("Estimated price in euro: "))
        if estimated_price > object.price:
            print("")
            print("Oh no, unfortunately the price you suggested is too high! 😨")
            print("")
        elif estimated_price < object.price:
            print("Oh no, unfortunately the price you suggested is too low! 😨")
            print("")
        else:
            print("Very good, you guessed the price of this object!")
            answer = input("Do you want to play again or get back to the commandbar?")
            if answer in ["play again", "play again!"]:
                priceguesser()
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                what_do_you_want_to_do()
    else:
        print(f"Sorry, you didn't guess the price. The correct price is {object.price} euros.")

# main

def main():
    login_or_signup()
    verify_data()  # Call to verify data after operations

###########################################################################################

try:
    main()
except Exception as e:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Ooops! PenguSystems {version}, has a bug and crashed! 😱")
    print(f"Error: {e}")
    print("Please contact the authors of this program to report this bug. 🤖")
    print("")

###########################################################################################
