# =======================tamrin4===========================
import random

error = 0
attempt = 0

computer = random.randint(1, 5)

for i in range(5):
    user_guess = int(input("please enter a number: "))
    attempt += 1
    if user_guess < computer:
        error += 1
        print("Guess higher")
        
    elif user_guess > computer:
        error += 1
        print("Guess lower")
        
    else:
        print("You guessed right - well done!")
        break
    
else:
    print(f"The hidden number is {computer}. You lost")
# ===========================tamrin5==================
library = {}
try:
    with open("library.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                book, author = line.split(":")
                library[book] = author
except FileNotFoundError:
    print("File not found. Starting with an empty library.")
while True:
    user = input("please enter one of the options below:\n add\nsearch\nshow\nexit: ").lower()
    if user == "add":
        book = input("please enter the name of the book: ").capitalize()
        author = input("please enter the name of the author: ").capitalize()
        library[book] = author
        
        with open("library.txt", "a", encoding="utf-8") as file:
            file.write(f"{book}:{author}\n")
            print("Successfully saved!")
    
    elif user == "search":
        book_name = input("please enter the name of the book: ").capitalize()
        if book_name in library:
            print(library[book_name])
        else:
            print("This book is not available!")
            
    elif user == "show":
        for book, author in library.items():
            print(f"{book}:{author}")
            
    elif user == "exit":
        print("Have a good day!")
        break
    
    else:
        print("The entered command is invalid. ")
# ===============================tamrin6======================

FILE_NAME = "inventory.txt"
inventory = {}
try:
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                commodity, quantity = line.split(":")
                inventory[commodity] = int(quantity)
except FileNotFoundError:
    print("File not found. Starting with an empty inventory.")
    
while True:
    print("add\nsell\nsearch\nshow\nsave\nreport\nexit")
    choice = input("please select one: ").lower()
    if choice == "add":
        commodity = input("please enter the product name: ").capitalize()
        quantity = int(input("please enter the quantity: "))
        if commodity in inventory:
            inventory[commodity] += quantity
        else:
            inventory[commodity] = quantity
            
    elif choice == "sell":
        name_product = input("please enter the product name: ").capitalize()
        amount = int(input("enter amount to sell: "))
        if name_product in inventory:
            if inventory[name_product] >= amount:
                inventory[name_product] -= amount
                if inventory[name_product] == 0:
                    del inventory[name_product]
            else:
                print("not enough stock")
        else:
            print("product not found.")
    elif choice == "search":
        name = input("please enter the name: ").capitalize()
        if name in inventory:
            print(inventory[name])
        else:
            print("product not found.")
            
    elif choice == "show":
        for commodity, quantity in inventory.items():
            print(f"{commodity}:{quantity}")
    elif choice == "save":
        with open(FILE_NAME, "a", encoding="utf-8") as file:
            for commodity, quantity in inventory.items():
                file.write(f"{commodity}:{quantity}\n")
        print("inventory saved to inventory.txt")
    elif choice == "report":
        total = len(inventory)
        total_stock = sum(inventory.values())
        max_quantity = -1
        max_item = ""
        min_quantity = float("inf")
        min_item = ""
        for commodity, quantity in inventory.items():
            if quantity > max_quantity:
                max_quantity = quantity
                max_item = commodity
            if quantity < min_quantity:
                min_quantity = quantity
                min_item = commodity
        print(f"total items: {total}")
        print(f"Total stock:{total_stock}")
        print(f"Most stocked item:{max_item} with {max_quantity} units")
    elif choice == "exit":
        print("Have a good day!🎉")
        break
    else:
        print("The entered command is invalid please try again.")
        
    
            
        
    