#ImportedObjects#

from getpass import getpass
import random

#version#

print("version: 2.01")
print("")

#classes#

class usr:
    def __init__(self, name, pw) -> None:
        self.name = name
        self.pw = pw

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

#definitions#

def load_users():
    try:
        with open("users.txt", "r") as file:
            for line in file:
                name, pw = line.strip().split(",")
                user_list.append(usr(name, pw))
    except FileNotFoundError:
        pass

def save_users():
    with open("users.txt", "w") as file:
        for user in user_list:
            file.write(f"{user.name},{user.pw}\n")

def login_or_signup():
    load_users()
    ok = False
    while ok == False:
        print("Do you want to login or signup?")
        answer = input("-> ")
        if answer in ["login", "log in"]:
            usrname = input("Enter your username: ")
            pw = getpass("Enter your password: ")
            for user in user_list:
                if usrname == user.name:
                    if pw == user.pw:
                        ok = True
                        print("")
                        print(f"Welcome on board {usrname}! 🚢")
                        what_do_you_want_to_do()  # Call what_do_you_want_to_do after logging in
                    else:
                        print("This password is incorrect, you will be sent back to the login process. 🔒")
                        break
            else:
                print("This username does not exist, you will be sent back to the login process. 🔒")
        elif answer in ["signup", "sign up"]:
            usrname = input("Enter your new username: ")
            pw = getpass("Enter your new password: ")
            user_list.append(usr(usrname, pw))  # Add the new user to the user_list
            save_users()  # Save the new user to the file
            ok = True
            print("")
            print(f"Welcome on board {usrname}! 🚢")
            what_do_you_want_to_do()  # Call what_do_you_want_to_do after signing up
        else:
            print(" -> Sorry pls answer with login or signup, thank you. 🤗")
def what_do_you_want_to_do():
    ok = False
    while ok == False:
        print("What do you want to do?")
        print("-> you can [logout] or play [priceguesser]")
        answer = input("-> ")
        if answer in ["logout", "log out"]:
            print("You've been locked out of the system 🔑")
            print("")
            ok = True
            login_or_signup()
        elif answer in ["priceguesser", "price guesser", "guesse the price"]:
            ok = True
            priceguesser()
        else:
            print(" -> Sorry pls answer with logout or priceguesser, thank you. 🤗")

def priceguesser():
    guessed = 0
    maxattempts = 5
    list_length = len(expensive_objects_list)
    print("")
    print("Welcome to PriceGuesser! 💰")
    print("Now you can guess the price of very expensive objects! 💸")
    print("")
    print("Ok let's start with the first very expensive object, the first expensive")
    object_number = random.randint(0,list_length-1)
    object = expensive_objects_list[object_number]
    print(f"object is a {object}.")
    print("")
    print(f"How expensive is this object? You have {maxattempts} attempts to guess the price.")
    while guessed < maxattempts:
        guessed += 1
        print(f"-> Attempt: {guessed}")
        estimated_price = int( input("Estimated price in euro: "))
        if estimated_price > object.price:
            print("")
            print("Oh no, unfortunately the price you suggested is too high! 😨")
            print("")
        elif estimated_price < object.price:
            print("Oh no, unfortunately the price you suggested is too low! 😨")
            print("")
        else:
            print("Very good, you guessed the price of this object!")
            break  # Break the loop when the user guesses correctly
    else:
        print(f"Sorry, you didn't guess the price. The correct price is {object.price} euros.")
def main():
    login_or_signup()

if __name__ == "__main__":
    main()