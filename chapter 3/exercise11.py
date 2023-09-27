gallons = float(input("Enter the gallons used(-1 to end):"))
miles = float(input("Enter miles driven:"))
total = miles / gallons
print(total)
gallon_count = gallons
miles_count = miles
inputs = int(input("Enter 1 to continue or press 0 to stop :"))
while inputs != 0:
    gallons = float(input("Enter the gallons used(-1 to end):"))
    gallon_count += gallons
    miles = float(input("Enter miles driven:"))
    miles_count += miles
    total = miles / gallons
    print(total)
    inputs = int(input("Enter 1 to continue or press 0 to stop"))
average = miles_count / gallon_count
print(average)






















# miles_per_gallons_used = miles / gallons
# counter = 0
# total = 0
# while True:
#     print("The miles/gallons=", miles_per_gallons_used)
#
#     gallons = float(input("Enter the gallons used(-1 to end):"))
#     if gallons == -1:
#         break
#     else:
#         miles = float(input("Enter miles driven:"))
#         miles_per_gallons_used = miles / gallons
#     total = total + miles_per_gallons_used
#
# print(total)
# gallons += 1

