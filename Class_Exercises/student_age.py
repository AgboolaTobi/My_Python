student_age_dict = {
    "dike": 33,
    "ope": 25,
    "melody": 20,
    "precious": 27
}


def student_age():

    name = input("Enter your name: ").lower()

    for key in student_age_dict.keys():
        if name == key:
            return f'Hi, {name}, you are {student_age_dict.get(key)} old...'
    else:
        age = input("Name not found, kindly enter your age: ")
        student_age_dict.update({name: age})
    return f'Hi, {name}, you are {age} years old... \n{student_age_dict}.'


print(student_age())
# students = {
#     "dike": 33,
#     "ope": 25,
#     "melody": 20,
#     "precious": 27
# }
#
#
# def student_age_correction():
#     name = input("Enter your name: ").lower()
#     for key in students.keys():
#         if name == key:
#             return f'Hi, {name} your age is {students.get(key)}'
#     else:
#         while name not in students.keys():
#             age = int(input("Name not found, enter your age: "))
#             students.update({name: age})
#             return f'Hi {name}, your age is {students.get(name)} \n {students}'
#
#
# print(student_age_correction())
