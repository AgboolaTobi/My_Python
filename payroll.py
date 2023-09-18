Employee_name = input("Enter name of employee:")

Number_hours_worked = float(input("Enter number of hours worked in a week:"))

Hourly_pay_rate = float(input("Enter hourly pay rate:"))
Gross_Pay = float(Hourly_pay_rate * Number_hours_worked)
Month = input("Enter month:")
Federal_tax_withholding_rate = int(input("Enter federal tax withholding rate:"))
State_tax_withholding_rate = int(input("Enter State tax withholding rate:"))
Federal_tax_withholding_rate = Gross_Pay * (Federal_tax_withholding_rate/100)
State_tax_withholding_rate = Gross_Pay * (State_tax_withholding_rate/100)
Total_Deduction = Federal_tax_withholding_rate + State_tax_withholding_rate
Net_pay = Gross_Pay - Total_Deduction
print(Employee_name,"Payroll statement for the month of",Month)
print("Employee's name:", Employee_name)
print("Hours Worked:", Hourly_pay_rate)

print("Pay Rate:$",Hourly_pay_rate)
Gross_Pay = Hourly_pay_rate * Number_hours_worked
print("Gross Pay:$",Gross_Pay)
print("Deductions: ")

print("Federal Withholding(20.0%):",Federal_tax_withholding_rate)
print("State Withholding (9.0%):$",State_tax_withholding_rate )
print("Total Deduction:$",Total_Deduction)
print("Net Pay:$",Net_pay)