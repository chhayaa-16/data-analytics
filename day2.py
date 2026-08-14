#====================day 2 -----que 1================== 
# company employee payroll system
# create var for -
# Employee_name 
# Empployee_Id
# Basic_salary
# HRA_percentag
# DA_percentage
# PF_percentage
# professional_tax
# Bonus

# calculate:
# HRA amount
# DA amount
# PF amount
# Gross salary
# total deduction 
# net salary

# finally compare:
# is net salary greater than 50000?
# is gross salary equal to net salary?
# is PF less than bonus?

# hint
 
# gross salary = basic + HRA + DA + Bonus
# net salary =   gross_salary - PF - professional tax
 




# code----

# Employee_name=input("Employee name : ")
# Empployee_Id=int(input("Emplyee ID : "))
# Basic_salary=int(input("Salary : "))
# HRA_percentage=int(input(" HRA % : "))
# DA_percentage=int(input(" DA % : "))
# PF_percentage=int(input(" PF % : "))
# professional_tax=int(input(" professional tax : "))
# Bonus=int(input(" Bonus : "))


# HRA = (Basic_salary * HRA_percentage) / 100
# print("HRA amount : ", HRA)

# DA  = (Basic_salary * DA_percentage) / 100
# print("DA amount : ", DA)

# PF = (Basic_salary * PF_percentage ) / 100
# print("PF amount : ", PF)


# gross_salary = Basic_salary + HRA + DA
# print("Gross salary : ",gross_salary)

# total_deduction = PF + professional_tax
# print("total Deduction : ",total_deduction)

# net_salaary = gross_salary - total_deduction
# print("net salary : ", net_salaary)



# ###compare

# net_salaary > 50000
# print("net salary greater than 50000 : ",net_salaary > 50000)


# gross_salary == net_salaary
# print("gross salary equal to net salary : ",gross_salary == net_salaary)

# PF < Bonus
# print("is PF less than bounus : ", PF < Bonus)





# -----------2. E-Commerce Shopping Bill-----------

# Create variables for:

# Laptop Price
# Mouse Price
# Keyboard Price
# Headphone Price
# Discount %
# GST %


# Calculate:

# Total Product Cost
# Discount Amount
# Price After Discount
# GST Amount
# Final Bill


# Compare:

# Is Final Bill greater than ₹1,00,000?
# Is Discount greater than GST?
# Hint
# Total
# ↓

# Discount

# ↓

# GST

# ↓

# Final Bill



#code-----
# Laptop_Price=int(input("Laptop Price : "))
# Mouse_Price=int(input("Mouse Price : "))
# Keyboard_Price=int(input("keyboard Price : "))
# Headphone_Price=int(input("Headphone Price : "))
# Discount_percentage=int(input("Discount % : "))
# GST_percentage=int(input(" GST % : "))


# total_cost= Laptop_Price + Mouse_Price  + Keyboard_Price + Headphone_Price
# print("total product cost : ",total_cost)

# discount_amount= ( total_cost  *  Discount_percentage) / 100
# print("Discount amount : ",discount_amount)

# discount_price= (total_cost - discount_amount)
# print("Price afetr discount : ",discount_price)

# GST_amount= (total_cost * GST_percentage) /100
# print("GST amount : ",GST_amount)

# final_bill= discount_price + GST_amount
# print("FINAL BILL : ",final_bill)


# #compare----

# final_bill < 100000
# print("final bill is greater than 100000 : ", final_bill < 100000)


# discount_price < GST_amount
# print("Is Discount greater than GST : ",discount_price < GST_amount)



# # 3. Bank Fixed Deposit Calculator 
# # Create variables for:

# # Principal Amount
# # Interest Rate
# # Time (Years)

# # Calculate:

# # Simple Interest
# # Maturity Amount

# # Now update maturity amount using

# # Bonus Interest
# # Tax Deduction

# # Compare

# # Is Maturity Amount greater than ₹2,00,000?
# # Is Interest equal to Principal?
# # Hint

# # Use

# # +=
# # -=

# # after calculating maturity amount.

# Principal__amnt=int(input("principle amount : "))
# interest_rate=int(input("interest rate : "))
# Time_Years=int(input("time (in years) : "))
# bonus_interest=int(input("Bonus interest : "))

# simple_interest = (Principal__amnt * interest_rate * Time_Years) / 100
# print("simple Interest : ", simple_interest)

# maturity_amount = Principal__amnt + simple_interest
# print("maturity amount : ",maturity_amount)



# maturity_amount += bonus_interest
# print("price after bonus interest :",maturity_amount)

# tax_deduction=




# --------------4. Student Marksheet Analyzer----------------

# Create variables for marks of 8 subjects.

# Calculate

# Total
# Average
# Percentage

# Now

# Add 5 grace marks to every subject
# Calculate new total
# Calculate new percentage

# Compare

# Old Percentage > New Percentage
# New Percentage >= 75
# Hint

# Reuse the same variables using +=.


# a=int(input("marks of Marathi : "))
# b=int(input("marks of English : "))
# c=int(input("marks of Hindi : "))
# d=int(input("marks of math : "))
# e=int(input("marks of sci : "))
# f=int(input("marks of geometry : "))
# g=int(input("marks of physics : "))
# h=int(input("marks of biology : "))


# total= a + b + c + d + e + f + g + h  
# print("total marks : ",total)

# avg= total / 8
# print("average of marks : ",avg)

# per = (total / 800) * 100
# print("percentage : ",per)

# a += 5
# b += 5
# c += 5
# d += 5
# e += 5
# f += 5
# g += 5
# h += 5

# #total after grace marks..

# new_total = a + b + c + d + e + f + g + h  
# print("total after add grace marks : ",new_total)

# new_per = (new_total / 800) * 100
# print(" New percentage : ",new_per)



# #compare

# per > new_per
# print("old percentage is gretaer than new percentage : ",per > new_per)
# new_per >= 75
# print("new percentage is greater than 75 : ",new_per >= 75)





# 5. Construction Cost Estimator 

# Create variables for

# Length
# Width
# Cement Cost per sq.ft
# Tiles Cost per sq.ft
# Labour Charge per sq.ft

# Calculate

# Total Area
# Cement Cost
# Tiles Cost
# Labour Cost
# Total Construction Cost

# Compare

# Is Labour Cost greater than Cement Cost?
# Is Total Cost above ₹5,00,000?



# Length=int(input("length : "))
# Width=int(input("width: "))
# Cement_Cost= int(input("cement cost per sq.ft : "))
# Tiles_Cost=int(input("tiles cost per sq.ft : "))
# Labour_Charge= int(input("labour charge per sq.ft : "))

# total_area= Length * Width
# print("total area ",total_area)


# total_cementCost = total_area * Cement_Cost
# print("toal cost of cement : ",total_cementCost)


# total_tilesCost = total_area * Tiles_Cost
# print("toal cost of Tiles : ",total_tilesCost)

# total_labourCost = total_area * Labour_Charge
# print("toal cost of Labours : ",total_labourCost)

# construction= total_cementCost + total_tilesCost + total_labourCost
# print("total cost of construction : ",construction)


# # compare


# total_labourCost < total_cementCost

# print("Is Labour Cost greater than Cement Cost :",total_labourCost < total_cementCost)

# construction < 500000
# print("Is Total Cost above ₹5,00,000 : ",construction < 500000)







# 6. Monthly Family Budget
# Create variables for

# Salary
# House Rent
# Food Expense
# Electricity Bill
# Internet Bill
# Petrol
# Entertainment
# Savings

# Calculate

# Total Expense
# Remaining Balance

# Now

# Update

# Add Bonus
# Deduct EMI
# Add Cashback

# Compare

# Remaining Balance > Savings
# Expense == Salary




# Salary=int(input("salary : " ))
# HouseRent=int(input("House rent : " ))
# FoodExpense=int(input("food expense : " ))
# ElectricityBill=int(input("Electricity Bill : " ))
# InternetBill=int(input("Internet Bill : " ))
# Petrol=int(input("petrol: " ))
# Entertainment=int(input("entertainment : " ))
# Savings=int(input("savings : " ))


# bounus=int(input("bonous : " ))
# EMI= int (input("add EMI : "))
# cashback= int(input("cashback : "))



# total_expense= Salary + HouseRent + FoodExpense + ElectricityBill + InternetBill + Petrol + Entertainment
# print ("total expence : ", total_expense)

# remaining_balance= Salary - total_expense
# print("remaining Balance : ",remaining_balance)

# # add bonus
# Salary += bounus 

# print("salary after bonous : ", Salary )

# #cut emi price
# Salary -= EMI 

# # print("Remaining Balance after EMIs :",Salary)

# # #add cashback

# # Salary += cashback
# # print("total amount : ", Salary )

# # # compare
# # Salary < Savings
# # print("salary is greater than savings : ",Salary < Savings)

# # total_expense == Salary
# # print("total expencse == saalary",total_expense == Salary)




# # 7. Cricket Tournament Statistics 
# # Create variables for

# # Total Runs
# # Total Balls
# # Total Fours
# # Total Sixes
# # Total Matches

# # Calculate

# # Strike Rate
# # Average Runs per Match
# # Boundary Runs
# # Boundary Percentage

# # Compare

# # Strike Rate > 150
# # Boundary Runs > Half of Total Runs
# # Hint

# # Boundary Runs

# # (Fours × 4) + (Sixes × 6)





# Total_Runs=int(input("total runs : "))
# Total_Balls=int(input("total balls : "))
# Total_Fours=int(input("total fours : "))
# Total_Sixes=int(input("total sixs : "))
# Total_Matches=int(input("total matches : "))



# strike_rate= (Total_Runs / Total_Balls) *100
# print("strike rate : ",strike_rate)


# average_runs = Total_Runs / Total_Matches
# print("average runs : ",average_runs)


# boundary_runs = (Total_Fours* 4) + (Total_Sixes * 6)
# print("boundry runs : ",boundary_runs)

# boundary_percentage = (boundary_runs / Total_Runs) * 100
# print("boundry percentage : ",boundary_percentage)




# strike_rate > 150
# print("Strike Rate > 150:", strike_rate > 150)


# strike_rate > 150
# print("Strike Rate > 150:", strike_rate > 150)



# =======================8. Mobile EMI Calculator 
# Problem

# Create variables for

# Mobile Price
# Down Payment
# Interest %
# EMI Months

# Calculate

# Loan Amount
# Interest Amount
# Total Payable
# Monthly EMI

# Compare

# EMI > ₹3000
# Loan Amount == Mobile Price


# mobilePrice = int(input("mobile price : "))
# downPayment = int(input("down payment : "))
# interestRate = int(input("interest rate : "))
# emiMonths = int(input("emi months : "))




# loan_amount = mobilePrice - downPayment
# print("Loan amount : ",loan_amount)


# interest_amount = (loan_amount * interestRate * emiMonths) / (100 * 12)
# print("Interest amount : ",interest_amount)



# total_payable = loan_amount + interest_amount
# print("toatal payble : ",total_payable)


# monthly_emi = total_payable / emiMonths
# print("monthly EMI : ", monthly_emi)




# monthly_emi > 3000
# print("EMI > ₹3000 :", monthly_emi > 3000)

# loan_amount == mobilePrice
# print("Loan Amount == Mobile Price :", loan_amount == mobilePrice)


# ======================9. Electricity Bill with Extra Charges
# Problem

# Create variables for

# Units
# Unit Rate
# Fixed Charge
# Fuel Charge
# Electricity Duty %
# GST %

# Calculate

# Energy Charge
# Subtotal
# Duty
# GST
# Final Bill

# Compare

# Final Bill > ₹5000
# GST > Fuel Charge


Units = 450
Unit_Rate = 8
Fixed_Charge = 200
Fuel_Charge = 500
Electricity_Duty = 5
GST = 18


Energy_Charge = Units * Unit_Rate
print("Energy Charge =", Energy_Charge)

Subtotal = Energy_Charge + Fixed_Charge + Fuel_Charge
print("Subtotal =", Subtotal)

Duty = (Subtotal * Electricity_Duty) / 100
print("Duty =", Duty)

GST_Amount = (Subtotal * GST) / 100
print("GST =", GST_Amount)

Final_Bill = Subtotal + Duty + GST_Amount
print("Final Bill =", Final_Bill)



print("Final Bill > ₹5000 :", Final_Bill > 5000)
print("GST > Fuel Charge :", GST_Amount > Fuel_Charge)






# 10. Complete Employee Performance Report (Master Challenge)
# Problem

# Create variables for

# Employee Name
# Employee ID
# Basic Salary
# Bonus
# Target Achieved
# Sales
# Attendance Percentage
# Working Days
# Leave Days

# Calculate

# Gross Salary
# Net Salary
# Daily Salary
# Salary per Working Day
# Average Sales per Day

# Update values using assignment operators:

# Add Performance Bonus
# Deduct Late Penalty
# Add Travel Allowance

# Now compare

# Net Salary > ₹75,000
# Attendance >= 95
# Sales > Target
# Leave Days == 0
# Working Days != Leave Days

# Finally print a well-formatted report.

# Hint

# Solve this in five steps:

# Create all variables.
# Perform arithmetic calculations.
# Update values using assignment operators (+=, -=).
# Perform relational comparisons (>, <, ==, !=, >=, <=).
# Print every calculated value and comparison result.



print("EMPLOYEE PERFORMANCE REPORT")
Employee_Name = "Chhaya patil"
print("Employee Name  :", Employee_Name)

Employee_ID = 1
print("Employee ID :", Employee_ID)

Basic_Salary = 60000
print("Basic Salary : ", Basic_Salary)

Bonus = 1000
print("Bonus : ", Bonus)


Target_Achieved = 500000
Sales = 550000
Attendance_Per = 96
Working_Days = 25
Leave_Days = 0


Gross_Salary = Basic_Salary + Bonus
print("Gross Salary : ", Gross_Salary)


Net_Salary = Gross_Salary

print("Net Salary: ", Net_Salary)


Daily_Salary = Basic_Salary / 30
print("Daily Salary  : ", Daily_Salary)

Salary_Per_Working_Day = Basic_Salary / Working_Days
print("Salary per Working Day : ", Salary_Per_Working_Day)


Average_Sales_Per_Day = Sales / Working_Days
print("Average Sales per Day  : ₹", Average_Sales_Per_Day)

Performance_Bonus = 5000
Net_Salary += Performance_Bonus
print("Performance Bonus : ", Performance_Bonus)


Late_Penalty = 2000
Net_Salary -= Late_Penalty
print("Late Penalty : ", Late_Penalty)

Travel_Allowance = 3000
Net_Salary += Travel_Allowance
print("Travel Allowance  : ", Travel_Allowance)

Salary_Check = Net_Salary > 75000

Attendance_Check = Attendance_Per>= 95

Sales_Check = Sales > Target_Achieved

Leave_Check = Leave_Days == 0

Working_Days_Check = Working_Days != Leave_Days


print("Target : ", Target_Achieved)
print("Sales  : ", Sales)
print("Attendance :", Attendance_Per, "%")
print("Working Days :", Working_Days)
print("Leave Days :", Leave_Days)

print("Net Salary > ₹75000 :", Salary_Check)
print("Attendance >= 95%  :", Attendance_Check)
print("Sales > Target  :", Sales_Check)
print("Leave Days == 0 :", Leave_Check)
print("Working Days != Leave  :", Working_Days_Check)

