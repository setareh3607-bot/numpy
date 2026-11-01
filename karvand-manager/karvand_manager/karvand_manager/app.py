# # =======================tamrin4===========================
# import random

# error = 0
# attempt = 0

# computer = random.randint(1, 6)

# for i in range(5):
#     user_guess = int(input("please enter a number: "))
#     attempt += 1
#     if user_guess < computer:
#         error += 1
#         print("Guess higher")
        
#     elif user_guess > computer:
#         error += 1
#         print("Guess lower")
        
#     else:
#         print("You guessed right - well done!")
#         break
    
# else:
#     print(f"The hidden number is {computer}. You lost")
# ===========================tamrin5==================
# library = {}
# try:
#     with open("library.txt", "r", encoding="utf-8") as file:
#         for line in file:
#             line = line.strip()
#             if line:
#                 book, author = line.split(":")
#                 library[book] = author
# except FileNotFoundError:
#     print("File not found. Starting with an empty library.")
# while True:
#     user = input("please enter one of the options below:\n add\nsearch\nshow\nexit: ").lower()
#     if user == "add":
#         book = input("please enter the name of the book: ").capitalize()
#         author = input("please enter the name of the author: ").capitalize()
#         library[book] = author
        
#         with open("library.txt", "a", encoding="utf-8") as file:
#             file.write(f"{book}:{author}\n")
#             print("Successfully saved!")
    
#     elif user == "search":
#         book_name = input("please enter the name of the book: ").capitalize()
#         if book_name in library:
#             print(library[book_name])
#         else:
#             print("This book is not available!")
            
#     elif user == "show":
#         for book, author in library.items():
#             print(f"{book}:{author}")
            
#     elif user == "exit":
#         print("Have a good day!")
#         break
    
#     else:
#         print("The entered command is invalid. ")
# # ===============================tamrin6======================

# FILE_NAME = "inventory.txt"
# inventory = {}
# try:
#     with open(FILE_NAME, "r", encoding="utf-8") as file:
#         for line in file:
#             line = line.strip()
#             if line:
#                 commodity, quantity = line.split(":")
#                 inventory[commodity] = int(quantity)
# except FileNotFoundError:
#     print("File not found. Starting with an empty inventory.")
    
# while True:
#     print("add\nsell\nsearch\nshow\nsave\nreport\nexit")
#     choice = input("please select one: ").lower()
#     if choice == "add":
#         commodity = input("please enter the product name: ").capitalize()
#         quantity = int(input("please enter the quantity: "))
#         if commodity in inventory:
#             inventory[commodity] += quantity
#         else:
#             inventory[commodity] = quantity
            
#     elif choice == "sell":
#         name_product = input("please enter the product name: ").capitalize()
#         amount = int(input("enter amount to sell: "))
#         if name_product in inventory:
#             if inventory[name_product] >= amount:
#                 inventory[name_product] -= amount
#                 if inventory[name_product] == 0:
#                     del inventory[name_product]
#             else:
#                 print("not enough stock")
#         else:
#             print("product not found.")
#     elif choice == "search":
#         name = input("please enter the name: ").capitalize()
#         if name in inventory:
#             print(inventory[name])
#         else:
#             print("product not found.")
            
#     elif choice == "show":
#         for commodity, quantity in inventory.items():
#             print(f"{commodity}:{quantity}")
#     elif choice == "save":
#         with open(FILE_NAME, "w", encoding="utf-8") as file:
#             for commodity, quantity in inventory.items():
#                 file.write(f"{commodity}:{quantity}\n")
#         print("inventory saved to inventory.txt")
#     elif choice == "report":
#         total = len(inventory)
#         total_stock = sum(inventory.values())
#         max_quantity = -1
#         max_item = ""
#         min_quantity = float("inf")
#         min_item = ""
#         for commodity, quantity in inventory.items():
#             if quantity > max_quantity:
#                 max_quantity = quantity
#                 max_item = commodity
#             if quantity < min_quantity:
#                 min_quantity = quantity
#                 min_item = commodity
#         print(f"total items: {total}")
#         print(f"Total stock:{total_stock}")
#         print(f"Most stocked item:{max_item} with {max_quantity} units")
#     elif choice == "exit":
#         print("Have a good day!🎉")
#         break
#     else:
#         print("The entered command is invalid please try again.")
# =========================================================================
# =========================================================================
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = "karvands.json"
DATA_DIR = os.path.join(BASE_DIR, "data")
FILE_PATH = os.path.join(DATA_DIR, FILE_NAME)

def load_data():
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    except FileNotFoundError:
        os.makedirs(DATA_DIR, exist_ok=True)
        data = {
            "bootcamp": "Maktab Sharif",
            "karvands": []
        }
        with open(FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        return data

def save_data(data):
        with open(FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
            
def next_id(data):
    
    karvands = data["karvands"]
    if not karvands:
        return 1

    ids = []
    for karvand in karvands:
        ids.append(karvand["id"])

    return max(ids) + 1

def add_karvand(data):
    new_id = next_id(data)
    name = input("Enter name: ")
    email = input("Enter email: ")
    city = input("Enter city: ")
    degree = input("Enter degree: ")
    field = input("Enter field: ")
    skill_name = input("Enter skill name: ")
    skill_level = input("Enter skill level: ")
    while True:
        try:
            skill_score = int(input("Enter skill score (0-100): "))
            if 0 <= skill_score <= 100:
                break
            print("Score must be between 0 and 100!")
        except ValueError:
            print("Please enter a valid number!")  
    new_karvand = {
        "id": new_id,
        "name": name,
        "email": email,
        "city": city,
        "education": {
            "degree": degree,
            "field": field
        },
        "skills": [
            {
                "name": skill_name,
                "level": skill_level,
                "score": skill_score
            }
        ]
    }

    data["karvands"].append(new_karvand)
    save_data(data)
    print("Karvand added successfully!")

def list_karvands(data):
    
    karvands = data["karvands"]

    if not karvands:
        print("No karvands found.")
        return       
    for karvand in karvands:
        
        karvand_id = karvand["id"]
        name = karvand["name"]
        city = karvand["city"]
        degree = karvand["education"]["degree"]
        field = karvand["education"]["field"]    
        print(f"ID: {karvand_id} | Name: {name} | City: {city} | Education: {degree} in {field}")
        skills = karvand["skills"]
        
        for skill in skills:
            
            skill_name = skill["name"]
            level = skill["level"]
            score = skill["score"]
            print(f"  - Skill: {skill_name} ({level}) - Score: {score}")
            
def search_karvand(data):
    
    karvands = data["karvands"]
    
    if not karvands:
        print("No karvands found.")
        return

    while True:
        try:
            target_id = int(input("Enter karvand ID to search: "))
            break
        except ValueError:
            print("Please enter a valid number!")

    found_karvand = None
    for karvand in karvands:
        if karvand["id"] == target_id:
            found_karvand = karvand
            break

    if found_karvand is None:
        print(f"No karvand found with ID {target_id}!")
        return
    
    
    karvand_id = found_karvand["id"]
    name = found_karvand["name"]
    email = found_karvand["email"]
    city = found_karvand["city"]
    degree = found_karvand["education"]["degree"]
    field = found_karvand["education"]["field"]

    print(f"ID: {karvand_id}")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"City: {city}")
    print(f"Education: {degree} in {field}")
    print("Skills:")
    for skill in found_karvand["skills"]:
        skill_name = skill["name"]
        level = skill["level"]
        score = skill["score"]
        print(f"  - {skill_name} ({level}): {score}")

def update_karvand(data):
    
    karvands = data["karvands"]

    if not karvands:
        print("No karvands found.")
        return

    while True:
        try:
            target_id = int(input("Enter karvand ID to update: "))
            break
        except ValueError:
            print("Please enter a valid number!")

    target_karvand = None
    for karvand in karvands:
        if karvand["id"] == target_id:
            target_karvand = karvand
            break

    if target_karvand is None:
        print(f"No karvand found with ID {target_id}!")
        return

    print("Press Enter without typing to keep the current value.")

    new_name = input(f"Enter new name ({target_karvand['name']}): ")
    if new_name != "":
        target_karvand["name"] = new_name

    new_city = input(f"Enter new city ({target_karvand['city']}): ")
    if new_city != "":
        target_karvand["city"] = new_city

    new_email = input(f"Enter new email ({target_karvand['email']}): ")
    if new_email != "":
        target_karvand["email"] = new_email

    save_data(data)
    print("Karvand updated successfully!")
def delete_karvand(data):
    
    karvands = data["karvands"]

    if not karvands:
        print("No karvands found.")
        return

    while True:
        try:
            target_id = int(input("Enter karvand ID to delete: "))
            break
        except ValueError:
            print("Please enter a valid number!")

    target_karvand = None
    for karvand in karvands:
        if karvand["id"] == target_id:
            target_karvand = karvand
            break

    if target_karvand is None:
        print(f"No karvand found with ID {target_id}!")
        return

    karvands.remove(target_karvand)
    save_data(data)
    print("Karvand deleted successfully!")
    
def generate_report(data):
    
    karvands = data["karvands"]

    total_karvands = len(karvands)
    total_skills = 0
    total_score = 0
    all_scores = []
    cities_set = set()
    unique_skills_set = set()

    for karvand in karvands:
        cities_set.add(karvand["city"])
        for skill in karvand["skills"]:
            total_skills += 1
            all_scores.append(skill["score"])
            unique_skills_set.add(skill["name"])

    if len(all_scores) > 0:
        average_skill_score = sum(all_scores) / len(all_scores)
        average_skill_score = round(average_skill_score, 2)
    else:
        average_skill_score = 0.0

    report_data = {
        "total_karvands": total_karvands,
        "total_skills": total_skills,
        "average_skill_score": average_skill_score,
        "cities": list(cities_set),
        "unique_skills": list(unique_skills_set)
    }

    report_path = os.path.join(DATA_DIR, "report.json")
    with open(report_path, "w", encoding="utf-8") as file:
        json.dump(report_data, file, indent=4)

    print("\n--- Summary Report ---")
    print(f"Total Karvands: {total_karvands}")
    print(f"Total Skills: {total_skills}")
    print(f"Average Skill Score: {average_skill_score}")
    print(f"Cities: {list(cities_set)}")
    print(f"Unique Skills: {list(unique_skills_set)}")
    print("Report saved to data/report.json successfully!\n")

def main_menu():
    print(FILE_PATH)
    
    data = load_data()

    while True:
        print("\n=== Karvand Management System ===")
        print("1. Add Karvand")
        print("2. List All Karvands")
        print("3. Search Karvand by ID")
        print("4. Search Karvand by Skill")
        print("5. Update Karvand")
        print("6. Delete Karvand")
        print("7. Summary Report")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_karvand(data)
        elif choice == "2":
            list_karvands(data)
        elif choice == "3":
            search_karvand(data)
        elif choice == "4":
            print("Skill search is optional.")
        elif choice == "5":
            update_karvand(data)
        elif choice == "6":
            delete_karvand(data)
        elif choice == "7":
            generate_report(data)
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main_menu()
