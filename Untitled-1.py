
# fruits = ["apple", "banana", "orange", "kiwi"]
# for fruit in fruits:
#     print(fruit)
# ======================================
# total = 0
# for i in range(1, 100, 2):
#     total += i
# print(total)
# =======================================
# contacts = {}

# while True:
#     contact = input("please enter add/search/show/count/exit:").strip().lower()
#     if contact == "add":
#         name = input("please enter name:").strip().lower()
#         phone = input("please enter phone:")
#         contacts[name] = phone
#     elif contact == "search":
#         name = input("please enter name:").strip().lower()
#         # if name in contacts:
#         #     print(contacts[name])
#         # else:
#         #     print("not found")
#         print(contacts.get(name, "not found"))
#     elif contact == "show":
#         for name, phone in contacts.items():
#         # for name in contacts:
#         #     print(contacts[name])
#             print(name, phone)
#     elif contact == "count":
#         try:
#             with open("contacts.txt", "r") as file:
#                 content = file.readlines()
#                 print(len(content))
#         except FileNotFoundError:
#             print("0")
#     elif contact == "exit":
#         with open("contacts.txt", "w") as file:
#             for name, phone in contacts.items():
#                 file.write(name+ ":"+ phone+ ","+ "\n")
#             print("save contacts")
#             break
#     else:
#         print("not found")
# ===================================================
# total = 0
# count = 0

# with open("contact.txt", "a") as file:
#     while True:
#         name = input("please enter name (or 'exit'): ").strip().lower()
#         if name == "exit":
#             break
#         age = input("please enter age: ")
#         file.write(f"{name} - {age}\n")

# with open ('contact.txt', 'r') as f:
#     for line in f:
#         name, age = line.split("-")
#         name = name.strip()
#         age = int(age.strip())
#         total += age
#         count += 1
#         print(f"Name:{name}, Age:{age}")
# average = total / count
        
# print(total)
# print(count)
# print(average)
# ===================================================
# students = {}

# try:
#     with open("students.txt", "r")as file:
#         for line in file:
#             name, grade = line.strip().split(":")
#             students[name] = grade
# except FileNotFoundError:
#     print("not found")

# while True:
#     x = input ("please enter add/ save/ show/ search/ exit: ")
#     if x == "add":
#         name = input("please enter name: ").strip().capitalize()
#         grade = input("grade: ")
#         students[name] = grade
#         print("save students")
#     elif x == "save":
#         with open("students.txt","w") as file:
#             for name, grade in students.items():
#                 file.write(name+ ":"+ grade+ "\n")
#         print("save")
#     elif x == "show":
#         for name, grade in students.items():
#             print(name+ ":"+grade+ "\n")
#     elif x == "search":
#         name = input("please enter name: ").strip().capitalize()
#         print(students.get(name, "not found"))
#     elif x == "exit":
#         break
#     else:
#         print("not found")
# ============================================================
# numbers = []

# for i in range(10):
#     number = int(input("please enter number: "))
#     if number not in numbers:
#         numbers.append(number)
# print(numbers)
# ===============================================================
# number = []

# for i in range(8):
#     number = int(input("enter a number: "))
#     numbers.append(number)
# ===========================
    