# try:
#     age = int(input("Enter your age: "))
#     if age > 0:
#         result = 10 / age
#         print(result)
# except ZeroDivisionError:
#     pass
# except ValueError:
#     print("Your age cannot be zero! Use your brain")
#
# # you can also do a tuple of exceptions like except(ZeroDivisionError, ValueError)
# finally:
#     print("Code run in spite the exception")


def age_check(value_of_age):
    if value_of_age <= 0:
        raise ValueError("Age cannot be less than or qual to zero")
    return f"You're {value_of_age} years old."


print(age_check(76))
