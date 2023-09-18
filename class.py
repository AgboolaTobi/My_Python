# age = int(input("Enter an age :"))
# if age < 18:
#     print("Not eligible")
#     if age >= 18 and age <= 60:
#         print("Eligible")
# else:
#     "Not Eligible"
import random

# result = "Not eligible" if age < 18 else "Eligible"
# print(result)

#
# language = input("""Enter a language of your choice
# 1. --> Yoruba
# 2. --> Igbo
# 3. --> Hausa
# """)
# match language:
#     case "1":
#         print("Welcome to Ibadan")
# Ibadan = input("""Your choice of Ibadan language
# 1. --> Core
# 2. --> Normal
# """)
# match Ibadan:
#     case "1":
#         print("You have selected core Ibadan language")
#     case "2":
#         print("You have selected normal Ibadan language")
#
#
#     case "2":
#         print("Welcome to Anambra")
#     case "3":
#         print("Welcome to Kano")
#     case _:
#         print("Not available")

#
# score = int(input("Enter your score: "))
#
# result = " "
# if score > 70:
#     result = "Pass with an A"
#
#     if score > 90:
#         result = "pass with distinction"
#
# else:
#     result = "fail"
# print(result)


# score = int(input("Enter your score: "))
#
# result = " "
# if 90 <= score <= 100:
#     result = "Distinction"
# elif 80 <= score < 90:
#     result = "Excellent"
# elif 70 <= score < 80:
#     result = "B grade"
#
# elif 60 < score < 70:
#     result = "C grade"
# elif 50 <= score < 60:
#     result = "D grade"
# elif score < 50:
#     result = "You failed the course! kindly pick another form next year"
#
# print(result)
# answer = f'Your score is {score * 5} \nYour result is {result}'
# print(answer)
# print(f'Your score is {score} \nYour result is {result}')
#
# print(bool(0))
# print(bool(5))
# print(bool(' '))
# print(bool('fhffhf'))
#
# name = input("Enter your name: ")
# if name:
#     print(f"your name is {name}")
#     x = 4
#     print(6 * x + 20)
# else:
#     print("No name entered!")
#     x = 3
#     y = 4
#     z = -2
#     print((2*x) + (4*y) - (z+5))


# To generate random numbers with in-built functions,use the randon built-in function
# The below will give random between 0 and 1
#
# _precious = random.random()
# print(_precious)
#
# _precious = random.randint(15, 100)
# print(_precious)
#
#
#
#
# while loop repeats a task as long as the condition is true. You have to set the condition to be false,else the loop will be infinite

#
# count = 0
# while count < 9:
#     print(random.randint(1, 21))
#
#     count += 1
#
# count = 0
# while count < 9:
#         print(count, random.randint(1, 21))
#         count += 1
#
#
# your program generate random number between 1 and 10,
# asks users to guess a number
# if user_input is incorrect, keep requesting for input.
# Once input is correct and matches the ramdom number,it should tell the user it is correct and stop
#
# print("""===Instructions===
# Guess a number between 1 and 3.
# Once your guessed input matches the displayed number. You win!""")

# user_guess =0
computer = (random.randint(1, 10))
user_guess = int(input("Enter your guess between 1 and 10: "))
print(computer)
while computer != u  ser_guess:
    user_guess = int(input("Enter your guess between 1 and 10: "))
    computer = (random.randint(1, 10))
    print(computer)
    print("You won!")



# guessed_number = random.randint(1, 10)
# guess = int(input("Enter your guessed number: "))
# while guessed_number != guess:
#     guess = int(input("Enter your guessed number: "))
