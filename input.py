# user = float(input("لطفا عدد اول را وارد کنید:"))
# user2 = float(input("لطفا عدد دوم را وارد کنید:"))
# if user > user2:
#     print(f"{user}")
# elif user < user2:
#     print(f"{user2}")
# else:
#     print("عدد با یکدیگر برابر است")
# ============================================
# number = float(input("please enter score:"))
# if number >= 90 and number >= 100:
#     print("A")
# elif number >= 80 and number < 90:
#     print("B")
# elif number >= 70 and number < 80:
#     print("C")
# elif number >=0 and number < 70:
#     print("مردود")
# else:
#     print("نمره نامعتبر")
# ======================================================
# number = int(input("please enter number:"))
# if number %2 == 0:
#     print(f"عدد زوج است")
# else:
#     print(f"عدد{number} فرد است")
# =====================================================
# number = float(input("please enter number one:"))
# operator = input("please enter +-*/")
# number2 = float(input("please enter number two:"))
# if operator == "+":
#     result = number + number2
#     print(result)
# elif operator == "-":
#     result = number - number2
#     print(result)
# elif operator == "*":
#     result = number * number2
#     print(result)
# elif operator == "/":
#     if number2 == 0:
#         print("تقسیم بر صفر امکان پذیر نیست")
#     else:
#         result = number / number2
#         print(result)
# else:
#     print("error")
# =========================================================
# age = int(input("please enter age :"))
# if age < 0:
#     print("سن نامعتبر")
# elif age < 12:
#     print("کودک")
# elif age <= 18:
#     print("نوجوان")
# elif age <= 60:
#     print("بزرگسال")
# else:
#     print("سالمند")
# ==========================================================
# number = int(input("Please enter number:"))
# while number >= 0:
#     print(number)
#     number = number - 1
# print("finish")
# ========================================================
# total_number = 0
# while True:
#     number = int(input("plese enter number  and Enter 0 to finish:"))
#     if number == 0:
#         break
#     total_number += number
# print(total_number)
# =========================================================
# password = "1234"
# while True:
#     user_password = input("Please enter password:")
#     if password == user_password:
#         print("wellcome")
#         break
#     else:
#         print("try again")
# ====================================================================
# import random


# number = random.randint(0, 10)
# while True:
#     user_guess = int(input("please enter between 0 and 10: "))
#     if user_guess == number:
#         print("you win")
#         break
#     elif number > user_guess:
#         print("Larger number")
#     else:
#         print("Smaller number")
# ==================================================================
import random

choices = ["rock", "paper", "scissors"]
    
user_score = 0
system_score = 0
while True:
    user_guess = input("Enter Rock, Paper, Scissors, or Exit:")
    if 