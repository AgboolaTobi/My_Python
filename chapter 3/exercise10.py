
principal = float(input("Enter your principal investment amount: "))
for years in range(1, 31):
    roi = principal * 0.07
    new_amount = roi + principal
    principal = new_amount
    print("Your ROI = $", round(roi, 2), "after", years,
          "years and your Investment going into the next investment cycle = $", round(principal, 2))

deposit = float(input("Enter your desired deposit amount: "))

for years in range(1, 31):
    roi = deposit * 0.07
    new_amount = deposit + roi
    deposit = new_amount
    print(f'your ROI is ${roi:.2f}, your investment is now ${new_amount:.2f}')