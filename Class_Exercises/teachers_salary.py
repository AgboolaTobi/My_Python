def your_salary():
    global gross_salary
    teachers_name = input("Enter teacher's name: ")
    month = input("Enter month: ")
    number_of_periods = int(input("Enter the total number of periods done in the month: "))
    rate = 20
    if 0 < number_of_periods <= 100:
        gross_salary = number_of_periods * rate
    elif number_of_periods > 100:
        (gross_salary) = (100 * rate) + (number_of_periods - 100) * 25
    return f'Teacher: {teachers_name} \nTotal Periods: {number_of_periods} periods for the month of {month}\nGross salary :$ {gross_salary}'


print("""
=========================
SEMICOLON MODEL SCHOOLS
=========================
""", your_salary())
print("""
=========================
""")
