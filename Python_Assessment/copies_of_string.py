number = int(input("Enter a value: "))
name = "toby"
result = number * name
print(result)


def my_result(name, number):
    if number != 0:
        result = name * number
    return result


(print(my_result("toby", 7)))

