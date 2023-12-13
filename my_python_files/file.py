with open("demo.txt", mode='w') as file:
    file.write("My name is Vera Ezeagu\n")
    file.write("I am tryng to open a python file\n")
    file.write("Let's see how well that works!")
with open("demo.txt", mode='a') as file:
    file.write("You're amazing!")

with open("demo.txt", mode='r') as file:
    print(f'{"first":<10}{"second":<10}{"third":<10}')
    for record in file:
        first, second, third, *fourth = record.split()
        print(f'{first:<10}{second:<10}{third:<10}')

try:
    with open("demo1.txt", mode='r') as datas:
        for data in datas:
            a, *b = data.split()
            print(a, *b)


except FileNotFoundError:
    x = 4
    print(x*x)
    print("make sure you check your file spelling")


print("program execution continues...")
