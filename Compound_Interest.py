principal = int(input("Enter your principal investment amount: "))
rate = int(input("Enter the rate: "))
for years in range(1, 31):
    profit = (principal * rate * years) / 100
    Total_return = principal + profit
    print("Your ROI = $", profit, "and your Investment going into the next investment cycle is= $", Total_return* years)