name = " arua "
print(name * 10)
print(f'[{2:^10}]')
s = "  shedrack  "
print(s.strip())
# to remove whitespaces from left or right, use lstrip or rstrip
# we can also capitalize the first character to uppercase
name = name.strip()
print(name.capitalize())
print(name.upper())
print(name.join("toby"))
print(" ".join(['a', 'b', 'c', 'd', 'e']))
print(name.count("a"))
name1 = input("Enter name: ").lower()
name2 = "precious"
print(name1 == name2)
print(ord('p'))
print(ord('P'))
print(name1 > name2)
if name2.startswith('p'):
    print("bad bitch")
name3 = "apple"
print(name2.index('p'))
print(name3.index('p'))
# to check the index count from the right,use the rindex
print(name3.rindex('p'))
print(name3.rindex('a'))
# the find method gives a result of 1 if the character is found in the string. it gives -1 if the character is not found
print(name3.find('w'))
# we also have the rfind
print(name3.rfind('e'))
# the in and not in operator gives a true or false
print('p' in name3)
print('p' not in name3)
if 'w' not in name3:
    print("it's a good day")

# startwith endwith method is to check if a word start or end with a string

cheecker1 = "abba"
cheecker2 = "abakaliki"
cheecker3 = "brada"
cheecker4 = "abraham"
cheecker5 = "anthony"
print(cheecker5.startswith('a'))
my_list = ["abba", "abakaliki", "brada", "abraham", "anthony", "prada", "train"]

list_check = []
for items in my_list:
    list_check.append(items.startswith('a'))
print(list_check)

# the splitting and joining strings
print(name3.replace('p', 's'))

semi = 'semi colon africa'
semi_result = semi.split()
print(semi_result)
semi2 = 'semicolon, africa, technology'
semi2_result = semi2.split(",")
semi3 = 'semicolonafricatechnology'
result_semi3 = semi3.split('o')
print(result_semi3)

# the join method takes and iterable and returns the items together

alphabets = ['A', 'B', 'C', 'D', 'E', 'F']
print("". join(alphabets))
print("-". join(alphabets))
print(" and ". join(alphabets))

# partition method... splits into three tuples based on its arguments i.e the part before it,the argument itself and
# the part after the argument
print(semi2.partition('m'))
print(semi2.partition("africa"))

# character testing method... The isdigit - checks if the method is called on numbers,isalum - checks if the method
# is called on all numbers.
sample_input = 'delighted'
print(sample_input.isdigit())
sample_input2 = "3402"
print(sample_input2.isdigit())
sample_input3 = 'ope-2003'
print(sample_input3.isalnum())

print(sample_input.strip(sample_input[0]))
