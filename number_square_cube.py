print("Number\t","Square\t","Cube\t\t")
number = 1
for number in range(1, 11):
    print(f'{number:>2}  {number*number:>8}  {number * number*number:>6}')