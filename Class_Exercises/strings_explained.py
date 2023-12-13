import re
import time

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
# name1 = input("Enter name: ").lower()
name2 = "precious"
# print(name1 == name2)
# print(ord('p'))
# print(ord('P'))
# print(name1 > name2)
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
print("".join(alphabets))
print("-".join(alphabets))
print(" and ".join(alphabets))

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
# raw strings
# allows us to treat our strings exactly the way it is. e.g to represent window file path
# file_path = 'C:\\MyFolder\\MySubFolder\\MyFile.txt'
# but with raw strings we can write exactly the way it is
# file_path = r'C:\MyFolder\MySubFolder\MyFile.txt'
# strip method will remove spaces around the string


word = "it's a boy"
print(word.upper().lower().title())
# the above is a chain method call
# regular expression
# can be used to match method or validate before a string is processed
# useful in web-scraping, transforming and cleaning data
# re module from psl(python standard library)

# metaCharacter

my_digit = '01234'
my_digit2 = '0808952954'
print(re.fullmatch(my_digit, '01234'))
print("True" if re.fullmatch(my_digit, '0808952954') else "False")
print("True" if re.fullmatch('\d{11}', '0808952954') else "False")
print("True" if re.fullmatch('\d\d\d\d\d\d\d\d\d\d\d', '01234') else "False")
print("True" if re.fullmatch(r'\w{11}', '08068952954') else "False")
# the below will return true if everything in the string is numeric
print("True" if re.fullmatch(r'\D{11}', '08068952954') else "False")
# the below would print would return true since we now have numeric
print("True" if re.fullmatch(r'\D{11}', 'preciouspre') else "False")

# character classes
# \d -> any digits 0-9
# \D -> any character that is not 0-9
# \s -> any white space character i.e spaces,tab,newline
# \S -> any character that is not whitespace
# \w -> alphanumeric character
# \W -> character that is not alphanumeric

# CUSTOM CHARACTER CLASS[]
# [aeiou] -> matches lowercase aeiou
# [A-Z] -> matches capital letter A to Z
# [a-z] -> matches lowercase letter a to z
# print(etc..)
# re.fullmatch(r'[A-Z][a-z]*', 'Asa')
# quantifier -> indicates zero or more occurrence of custom class it follows
# ^ quantifer -> indicates character that is not specified. ->
# Example: 'Match if re.fullmatch([^a-z]', 'A') else 'No Match' output
# the * and + are greedy,they match 1 or more
print("True" if re.fullmatch(r'[A-Z][a-z]*', 'Toby') else "False")
print("True" if re.fullmatch(r'[A-Z]*[a-z]*', 'AGgboolatoby') else "False")
# ^ quantifier -> indicates character that is not specified
print("True" if re.fullmatch(r'[A-Z]+[a-z]*', 'Toby') else "False")
print("True" if re.fullmatch(r'[A-Z]*[a-z]+', 'AGgboolatoby') else "False")
# the  below means 2 or more
print("True" if re.fullmatch(r'[A-Z]{2,}', 'AGgboolatoby') else "False")
# between 2 and 6
print("True" if re.fullmatch(r'[A-Z]{2,6}', 'AGgboolatoby') else "False")
# ? matches zero or one occurrence of a sub expression
'Yes' if re.fullmatch('labell?ed', 'labelled') else 'Yes'
'Yes' if re.fullmatch('label?ed', 'labeled') else 'Yes'
'Yes' if re.fullmatch('labell?ed', 'labellled') else 'No'

# Replacing Substring & Splitting String
# the sub replaces all pattern in a string. Example: re.sub(r'\t',',','1\t2\t3\t4') -> '1, 2, 3, 4'
# it receives 3 arguments
# the pattern to match
# the replacement text (',') and
# the string to be searched ('1\t2\t3\t4')

# {n,} -> matches at least n occurrence or more
Example: 'Found' if re.fullmatch(r'\d{3,}', '123') else 'Not found'
# {n,m} -> matches between n and my_digit2
example: 'Yes' if re.fullmatch(r'\d{3,6}', '123') else 'No'

# READ ABOUT THE PYTHON RE MODULE
toby = re.split(r',\s*', '1, 2, 3, 4, 5, 6, 7 ,8')
toby2 = re.split(r' *', '12345678')
print(toby)

print(toby2)
# Restricting matches to beginning or end of string
# ^ metacharacter restrict match to the beginning of a string
# e.g result = re.search('^Esther','Esther and Eddie')(the caret ^ will negate. it will match anything that is not Esther)
# result.group if result else 'No'

# $ metacharacter placed at the end of a regular expression indicate matching at the end of a string
# e.g result = re.search('python$', 'python is fun')(the $ sign metacharacter is used to check is a string ends with a particular word
# result.group() if result else "No"
# Output: 'not fund'

# Function findall finds every match substring in a string and returns a list of matching substrings
# example: contact = 'Eddie Esther, Home: 080-694-0144, Work: 0803-444-0144'
# re.findall(r'\d{4}-\d{3}-\d{4}', contact)
# output: ['0802-694-0144', '0803-444-0144']

# Function finditer works like findall but returns a lazy iterable of match object. finditer saves memory because it returns its matches one a time.
# Example: for phone in re.finditer(r'\d{3}- \d{3}-\d{4}', contact):
#     0802-694-0144
#     0803-444-0144

# Files I/O
# Variables, list, set, tuple, dictionary etc all store information temporarily. Data stored in variables are lost when they get out of a scope or program terminate
# Files provide long term retention of large data even after the program terminates. Data stored in files are persistent
#
# You want your program/script to interact with other part of the system such as take input from other components,interact with files or image etc...

# Types of files
# Text files
# Image files
# Audio files
# PDF files
# JSON
#
# Python scripts/programs can be used to create, update and process data files

# Reading text from a file
with open("account.txt", mode='r') as accounts:
    print(f'{"Account":<10}{"Name":<10}{"Balance":>10}')
    for record in accounts:
        account, name, balance = record.split()
        print(f'{"Account":<10}{"Name":<10}{"Balance":>10}')
