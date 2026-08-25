

# # #partA : arithmetic operator
# # #Q-1 Employee Salary Calculator
# # Create variables to store:
# # Basic Salary 
# # Calculate:
# # HRA (20% of Basic Salary) 
# # DA (15% of Basic Salary) 
# # PF (12% of Basic Salary) 
# # Net Salary 
# # Display all values.






# basic_Salary=25000                                            basic_salary=int(input("enter basic salary : "))
# # print("Basic Salary :", basic_Salary)

# hra=basic_Salary*20/100
# print("HRA (20%):", hra)

# da=basic_Salary*15 / 100
# print("DA (15%):", da)

# pf=basic_Salary * 12 / 100
# print("PF (12%):", pf)

# net_salary = basic_Salary + hra + da - pf
# print("Net Salary:", net_salary)







# #2-Student Result
# Create variables for marks of five subjects.
# Calculate:
# Total Marks 
# Average Marks 
# Percentage 
# Display all results.




# math=79
# eng=68
# sci=78
# hindi=88
# marathi=58

# num_of_subject=5
# max_marks=500

# print ("student result")
 
# print("marks of mathematics:",math)
# print("marks of English:",eng)
# print("marks of Science:",sci)
# print("marks of hindi:",hindi)
# print("marks of marathi:",marathi)


# total_marks= math + eng + sci + hindi + marathi 
# avg=total_marks / num_of_subject
# percentage=(total_marks / max_marks)*100


# print( "sum of all marks:  ",total_marks)
# print("average of marks:  ",avg)


# Q3-- Rectangle Calculator
# Problem
# Create variables for:
# Length 
# Width 
# Calculate:
# Area 
# Perimeter 



# length=20
# width=5


# area= length * width 
# print("Area of Rectangle is: ",area)

# perimeter = 2 * (length + width)
# print("Perimeter of Rectangle is:", perimeter)


# Q4----Petrol Expense Calculator
# Create variables for:
# Distance 
# Mileage 
# Petrol Price 
# Calculate:
# Fuel Required 
# Total Expense 





# # distance=80
# mileage=15
# petrol_Price=100 

# fuel_required = distance / mileage
# total_expense = fuel_required *petrol_Price

# print("Distance:", distance,)
# print("Mileage:", mileage,)
# print("Petrol Price:", petrol_Price)

# print("Fuel Required:", fuel_required,)
# print("Total Expense:", total_expense)



# #Q5 --- GST calculator 

# Problem
# Create a variable for product price.
# Calculate:
# GST (18%) 
# Final Price 
# Hint
# GST
# Price × 18 /100
# Final Price
# Price + GST





# product_price=int(input("enter product price : "))
# # gst=(product_price * 18 ) / 100
# print(gst)

# final_price=(product_price + gst)
# print(final_price)







# Question 6 – Time Converter
# Problem
# Create a variable storing total seconds.
# Convert it into:
# Hours 
# Minutes 
# Seconds 
# Hint
# Use
# Floor Division (//) 
# Modulus (%) 


# Logic
# Seconds
#    ↓
# Hours

# Remaining Seconds
#       ↓
# Minutes

# Remaining Seconds





# sec=int(input("Enter seconds :"))
# print("total seconds : ",sec)
# hours=(sec / 3600 )
# print("Hours : ",hours)

# minute=(sec / 60 )
# print("Minute : ",minute)

# seconds=(sec % 60 )
# print("Second : ",seconds)

# Question 7 – Currency Converter
# Problem
# Create variables for:
# Amount in INR 
# USD Exchange Rate 
# Convert INR into USD.
# Hint
# USD = INR / Rate




# Amount=int(input("amount in INR : "))
# USD_Exchange_Rate=2

# USD=Amount / USD_Exchange_Rate
# print("USD :",USD)





# #Question 8 – Cricket Strike Rate
# Problem
# Create variables for:
# Runs 
# Balls Played 
# Calculate Strike Rate.
# Hint
# Strike Rate

# Runs ×100
# ----------
#  Balls






# print("Score Board")
# Runs=98
# Balls_played=45

# strike_rate= (Runs*100) / Balls_played
# print("Runs",Runs)
# print("Balls played-",Balls_played)
# print("the strike rate is:",strike_rate)





# #Question 9 – Circle Calculator
# Problem
# Create variables for:
# Radius 
# Pi 
# Calculate:
# Area 
# Circumference 
# Hint
# Area
# π × r²
# Circumference
# 2 × π × r






# Radius=10
# pi=7.14

# print("Radius",Radius)
# print("pi",pi)

# area=pi*Radius**2
# Circumference= 2*pi*Radius

# print("area of circle:",area)

# print("Circumference of circle:",Circumference)












# #Question 10 – Cube Calculator
# Problem
# Create a variable for side.
# Calculate:
# Volume 
# Total Surface Area 
# Hint
# Volume
# Side³
# Surface Area
# 6 × Side²






# side = 5

# volume = side * side * side
# surface_area = 6 * side **2

# print("Side:", side)
# print("Volume of Cube:", volume)
# print("Total Surface Area of Cube:", surface_area)

# Part B – Assignment Operators--------------
# #Question 11 – Wallet Balance
# Problem
# Create variables to store:
# Basic Salary 
# Calculate:
# HRA (20% of Basic Salary) 
# DA (15% of Basic Salary) 
# PF (12% of Basic Salary) 
# Net Salary 
# Display all values.







# balance = 10000

# print("Balance:", balance)

# balance += 500
# print("Add Salary:", balance)

# balance -= 1500
# print("Shoppingexpence :", balance)

# balance -= 300
# print("Recharge:", balance)

# balance += 100
# print("Add Cashback:", balance)


# #Question 12 – Bank Account
# Create a variable named balance.
# Perform:
# Deposit 
# Withdraw 
# Add Interest 
# Hint
# Keep updating the same variable.





# balance=int(input ("Enter Balance : " ))

# balance += 5000
# print("Deposit money:", balance)

# balance -= 1500
# print("withdrawl maoney:", balance)

# balance * 2
# print("balance after add interest : ",balance)

# Question 13 – Student Marks Update
# Create a variable named marks.
# Perform:
# Add Grace Marks 
# Multiply by Bonus 
# Divide Marks 



# marks=72
# print("marks:",marks)

# marks += 10
# print("Including grace marks:", marks)

# marks *=2
# print("Add bonus marks:", marks)

# marks /= 2
# print("Divide marks:", marks)

# Question 14 – Inventory Management
# Problem
# Create a variable named stock.
# Update stock after:
# Purchase 
# Sale 
# Damaged Items 
# Hint
# +=
# -=





# stock=int(input("Enter stock number : "))
# purchase=int(input("Enter purchase number : "))
# sales=int(input("Enter sale number : "))
# damaged_item=int(input("Enter Damaged items : "))


# stock += purchase
# print("Stock after purchase : ",stock)

# stock -= sales
# print("Stock after sale : ",stock)


# stock -= damaged_item
# print("Stock after damaged items : ",stock)



# Question 15 – Shopping Cart
# Problem
# Create a variable named total.
# Add prices of three products.
# Subtract discount.
# Hint
# Keep updating one variable only.



# total= 1000
# print("The value 1st product : ",total)

# total += 500 
# print("The value 2st product : ",total)

# total += 200
# print("The value 3st product : ",total)

# total -=100
# print("total : ",total)






# Question 16 – Mobile Data Balance
# Problem
# Create a variable named data_balance.
# Perform:
# Data Usage 
# Data Recharge 
# Hint
# Use
# -=
# +=




# data_balance=500
# print("Available Balance:",data_balance)

# data_balance -=20
# print("Data used:",data_balance )

# data_balance += 1000
# print("Data Recharge:",data_balance )









# Question 17 – Population Growth
# Problem
# Create a variable named population.
# Increase population by 10%.
# Hint
# population += population * 10 /100







# population=14000
# print("Total Population:",population)

# population += population * 10 /100
# print("Population after increasing by 10 percent:",population)






# #Question 18 – Number Transformation
# Problem
# Create a variable named number.
# Perform:
# Add 
# Multiply 
# Floor Divide 
# Modulus 
# Power 
# Hint
# Use
# +=
# *=
# //=
# %=
# **=







# number=100
# print("given number:",number)

# number += 50 
# print(" After Add:",number)


# number *=2
# print(" After Multiply:",number)

# number //=2
# print(" After Floor Divide:",number)

# number %=2
# print(" After Modulus:",number)

# number **=2
# print(" After Power:",number)











# #Question 19 – Game Score----

# problem
# Create a variable named score.
# Perform:
# Bonus 
# Penalty 
# Double Score 
# Half Score 
# Hint
# Use assignment operators only.






# score=87
# print("score:",score)

# score += 20
# print(" After Add bonus score:",score)

# score *2 
# print(" After Double score:",score)

# score /2
# print("Half score:",score)


# #Question 20 – Savings Account
# Problem
# Create a variable named saving.
# Update balance after:
# Deposit 
# Withdrawal 
# Interest 
# Hint
# Use
# +=
# -=






# saving=50000
# print("thr amount in account",saving)

# saving += 50000
# print("Update balance after deposit :",saving)

# saving -= 25000
# print("Update balance after withdrawal :",saving)

# saving +=500
# print("Update balance after add interest :",saving)










# ----------------Part C – Relational Operators
# Question 21 – Compare Two Numbers
# Create two number variables.
# Print the result of:
# Greater Than 
# Less Than 
# Equal To 
# Not Equal To 
# Greater Than Equal To 
# Less Than Equal To 
# Hint
# Store each comparison inside a variable.







# a=100
# b=175

# if (a>b):
#  print("the value of {a} is greater than {b}")
# else:
#  print("{a}is not greater that {b}")

# if (a<b):
#  print("the value of {a} is less than {b}")
# else:
#  print("{a}is not less that {b}")


# Question 22 – Compare Student Marks
# Create marks for two students.
# Compare both students using all relational operators.




# stu1=int(input("marks of 1st student : "))
# stu2= int(input("marks of 2nd student : "))

# stu1 == stu2
# print(stu1 == stu2) 

# stu1 != stu2
# print(stu1 != stu2) 

# stu1 >= stu2
# print(stu1 >= stu2) 

# stu1 <= stu2
# print(stu1 <= stu2)

# stu1 > stu2
# print(stu1 > stu2) 

# stu1 < stu2
# print(stu1 < stu2) 





# Question 23 – Compare Salaries
# Create salary variables for two employees.
# Compare them using all relational operators.






# emp1=int(input("enter salary of 1st employee : "))
# emp2= int(input("enter salary of 2nd employee  : "))

# emp1 == emp2
# print(emp1 == emp2) 

# emp1 != emp2
# print(emp1 != emp2) 

# emp1 >= emp2
# print(emp1 >= emp2) 

# emp1 <= emp2
# print(emp1 <= emp2)

# emp1 > emp2
# print(emp1 > emp2) 

# emp1 < emp2
# print(emp1 < emp2) 


# Question 24 – Compare Product Prices
# Create prices of two products.
# Compare them.


# price1= 500
# price2= 700


# print("price1 == price2 :", price1 == price2)
# print("price1 != price2 :", price1 != price2)
# print("price1 > price2  :", price1 > price2)
# print("price1 < price2  :", price1 < price2)
# print("price1 >= price2 :", price1 >= price2)
# print("price1 <= price2 :", price1 <= price2)





# Question 25 – Compare Ages
# Create ages of two people.
# Print all comparison results.



# age1 = 20
# age2 = 25

# print("age1 == age2 :", age1 == age2)
# print("age1 != age2 :", age1 != age2)
# print("age1 > age2  :", age1 > age2)
# print("age1 < age2  :", age1 < age2)
# print("age1 >= age2 :", age1 >= age2)
# print("age1 <= age2 :", age1 <= age2)



# Question 26 –
# Compare Heights Create height variables.
# Compare them



# peole_height1 = 123
# people_height2 = 187

# print(people_height1 ==people_ height2)
# print( people_height1 !=people_height2)
# print( people_height1 > people_height2)
# print(people_height1 < people_height2)
# print( people_height1 >= people_height2)
# print( people_height1 <= people_height2)



# Question 27 – Compare Cricket Scores
# Create scores of two teams.
# Compare them.


# team1 = 156
# team2 = 143


# print( team1 == team2)
# print( team1 != team2)
# print( team1 > team2)
# print(team1 < team2)
# print(team1 >= team2)
# print( team1 <= team2)







# Question 28 – 
# Compare Temperatures
# Create morning and afternoon temperatures.
# Compare them.




# morning_temp = 34
# afternoon_temp = 45



# print( morning_temp == afternoon_temp)
# print( morning_temp != afternoon_temp)
# print( morning_temp > afternoon_temp)
# print( morning_temp < afternoon_temp)
# print( morning_temp >= afternoon_temp)
# print(morning_temp <= afternoon_temp)






# Question 29 –
# Compare Mobile Prices
# Create prices of two mobile phones.
# Compare them.


# mobile1 = 40000
# mobile2 = 60500



# print( mobile1 == mobile2)
# print( mobile1 != mobile2)
# print( mobile1 > mobile2)
# print( mobile1 < mobile2)
# print( mobile1 >= mobile2)
# print( mobile1 <= mobile2)



# Question 30 – Equality Checker
# Create two number variables.
# Print the result of:
# == 
# != 
# > 
# < 
# >= 
# <= 
# Hint
# Every comparison returns either:
# True 
# False



# num1 = 34
# num2 = 70

# print( num1 == num2)
# print( num1 != num2)
# print(num1 > num2)
# print( num1 < num2)
# print( num1 >= num2)
# print( num1 <= num2)


















# a==b
# # .
# # .
# # .
# # .
# # .
# # .
# # .
# # .
# # .
# # .
# # .

# # ..
# # ..
# # .
# # ..

# # .
# #---------------------- #day 3
# pin=1234
# balance=20000

# var=int(input("enter your pin"))

# if pin==var:
#  print("valid pin")
# else:
#  print("invalid pin")


# if balance<=5000:
#   print("yes")

# elif balance ==20000:
#  print("y")

# elif balance>=20000:
#  print("no")

# else:
#  print("invalid balance")
   



# ####------for loop


# for i in range (20):
#  a +=2                      #add 2 
#  print(a)
# print(a)




# count=5
# while count>=0:
#  count-=0
#  print(count)
# print(count) 

# a=1
# while a <= 100:
#     if a == 10 or a == 30 or a == 40:
#         a += 1
#         continue

#     print(a)
#     a += 1


# a=1
# while a <=10:
#     if a == 2 or a == 4 or a == 8:
#         a += 2
#         continue
#     print(a)
#     a +=2