import datetime
import random
import uuid
import math


# 1️⃣ Current Time Function
def current_time():
    return datetime.datetime.now()


# 2️⃣ Random Number Function
def random_number():
    return random.randint(1, 100)


# 3️⃣ UUID Function
def create_uuid():
    return uuid.uuid4()


# 4️⃣ File Write Function
def write_file(name, text):
    f = open(name, "w")
    f.write(text)
    f.close()
    return "File Saved Successfully"


# 5️⃣ Explore Function
def explore_module(module):
    return dir(module)


# 6️⃣ Menu Function
def menu():

    while True:

        print("\n--- Multi Utility Toolkit ---")
        print("1. Show Current Time")
        print("2. Random Number")
        print("3. Generate UUID")
        print("4. Write File")
        print("5. Explore Math Module")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Current Time:", current_time())

        elif choice == "2":
            print("Random Number:", random_number())

        elif choice == "3":
            print("UUID:", create_uuid())

        elif choice == "4":
            name = input("Enter file name: ")
            text = input("Enter text: ")
            print(write_file(name, text))

        elif choice == "5":
            print(explore_module(math))

        elif choice == "6":
            print("Program Exit")
            break

        else:
            print("Wrong Choice")


# Important Line
if __name__ == "__main__":
    menu()