gallons = float(input("Enter the gallons used(-1 to end):"))
miles = float(input("Enter miles driven:"))
miles_per_gallons_used = miles / gallons
counter = 0
total = 0
while True:
    print("The miles/gallons=", miles_per_gallons_used)
    if gallons == -1:
        break
    gallons = float(input("Enter the gallons used(-1 to end):"))
    miles = float(input("Enter miles driven:"))
    miles_per_gallons_used = miles / gallons
    total = total + miles_per_gallons_used

print(total)
gallons += 1
