# #Student Performance Analyzer
#que 1 

# print("Student academic performance")

# number_of_sub=5
# Name=input("Enter Student Name  : ")

# print("SCORE CARD")

# python=int(input("Enter Python marks  : "))
# sql=int(input("Enter SQL marks : "))
# excel=int(input("Enter EXCEL marks : "))
# stat=int(input("Enter Statistics marks : "))
# power_bi=int(input("Enter POWER BI marks : "))



# total_marks = python + sql + excel + stat + power_bi
# print("total Marks   :  ",total_marks)

# per = (total_marks/500)*100
# print("percentage  : ",per)


# if python >= 35 and sql >= 35 and excel >= 35 and stat >= 35 and power_bi >= 35:
#     print(" Status   :  PASS")
# else:
#     print(" Status   :  FAIL")





# if per <= 95:
#     print(" Grade A+")
# elif per <= 90:
#     print("A")
# elif per <=70:
#     print("B")
# elif per <= 60:
#     print("C")
# else:
#     ("Grade : FAIL")



#  Employee Salary Analytics


# E_Name=input("Employee Name  :  ")
# Basic_Salary=int(input("Sallary in month : "))
# HRA=int(input("HRA : "))
# DA=int(input("DA : "))
# Tax=int(input("TAX : "))
# Bonus=int(input("Bonus : "))



# Gross_salary= Basic_Salary + HRA + DA
# print("Gross Salary :  ",Gross_salary)

# Net_salary= Gross_salary - Tax 
# print("Net Salary : ",Net_salary)

# annual_salary= Basic_Salary * 12
# print("Annual Salary : ", annual_salary)


# if annual_salary <= 800000:
#     print("Eligible for Bonus")
# else:
#      print("Not Eligible for Bonus")



# --------------Assignment – 03
#Product Sales Dashboard

# Product_Name = input("Enter product Name : ")
# Product_Price =int(input("Enetr product price : "))
# Quantity_Sold = int(input("Enter Quantity sold : "))
# GST = int(input("GST in %   : "))
# Discount = int(input("Discount in %  : "))

# # gross_sale = Quantity_Sold * Product_Price
# # print ("Goss sale : ",gross_sale)

# # GST_Amount=(Product_Price * GST) / 100
# # print ("GST Amount : ",GST_Amount)

# # Discount_amount=(Product_Price * Discount) / 100
# # print ("GST Amount : ",Discount_amount)

# # Final_Revenue= (gross_sale - Discount_amount) + GST_Amount
# # print ("Final_Revenue: ",Final_Revenue)


# # if Final_Revenue >= 50000:
# #     print(f"{Product_Name} is a Top performer ")
# # else:
# #     print("no")


# # Assignment – 04
# # Customer Purchase Analysis

# C_Name=input("Enter customer Name : " )
# Purchase_Amount=int(input("Enter Purchase amount : "))
# Membership= input("Membership (Yes/No): ")
# Coupon_Applied= input("Coupon (Yes/No): ")

# discount = 0

# if member=="Yes":
#     discount += purchase*0.10

# if coupon=="Yes":
#     discount += purchase*0.05

# amount = purchase-discount
# gst = amount*0.18
# bill = amount+gst

# print("Final Bill:", bill)

# if bill>10000:
#     print("Premium Customer")
# else:
#     print("Regular Customer")


# #Que-----5
# #Sales Executive KPI Analysis    

# name = input("Executive Name: ")

# target = int(input("Target: "))
# sales = int(input("Actual Sales: "))
# rating = float(input("Customer Rating: "))

# achievement = sales/target*100

# print("Achievement:",achievement,"%")

# if achievement>=100:
#     incentive=10000
# else:
#     incentive=5000

# print("Incentive:",incentive)

# if achievement>=100 and rating>=4:
#     print("Promotion Eligible")
# else:
#     print("Not Eligible")


# #Assignment – 06
# #Attendance Analytics


# name=input("Student Name: ")

# total=int(input("Total Classes: "))
# attended=int(input("Attended Classes: "))

# percent=attended/total*100

# print("Attendance:",percent)

# if percent>=75:
#     print("Eligible for Exam")
# else:
#     print("Not Eligible")

# if percent>=90:
#     print("Grade A")
# elif percent>=75:
#     print("Grade B")
# else:
#     print("Grade C")





# Assignment – 07
# Electricity Consumption Analysis


# name=input("Consumer Name: ")

# previous=int(input("Previous Reading: "))
# current=int(input("Current Reading: "))
# rate=float(input("Rate per Unit: "))

# units=current-previous
# bill=units*rate
# gst=bill*0.18
# final=bill+gst

# print("Units:",units)
# print("Final Bill:",final)

# if units>500:
#     print("High Consumption Alert ")
# else:
#     print("Normal")


# Assignment – 08
# Loan Eligibility Analyzer



# name=input("Name: ")

# age=int(input("Age: "))
# salary=int(input("Monthly Salary: "))
# emi=int(input("Existing EMI: "))
# cibil=int(input("CIBIL Score: "))

# ratio=emi/salary*100

# print("EMI Ratio:",ratio)

# if cibil>=750 and ratio<40:
#     print("Loan Approved")
# else:
#     print("Loan Rejected")



# Assignment – 09
# Inventory Analytics

# product=input("Product Name: ")

# opening_stock=int(input("Opening Stock: "))
# purchase=int(input("Purchased Stock: "))
# sold=int(input("Sold Stock: "))

# closing_stock=opening_stock+purchase-sold

# print("Closing Stock:",closing_stock)
# if closing<20:
#     print("Reorder Required")
# else:
#     print("Stock Available")



#     name=input("Patient Name: ")

# weight=float(input("Weight: "))
# height=float(input("Height in Meter: "))

# bmi=weight/(height*height)

# print("BMI:",bmi)

# if bmi<18.5:
#     print("Underweight")
# elif bmi<25:
#     print("Normal")
# else:
#     print("Overweight")


# Assignment – 10
# Hospital Patient Analytics


# p_name=input("Enter patient name : ")
# Age=int(input("Enter Age :" ))
# Weight=int(input("Enter Weight :" ))
# Sugar_level=int(input("Enter sugar Level :" ))
# BP=int(input("Enter BP :" ))




#Assignment – 11
#Bank Transaction Analyzer


# Assignment – 14
# Social Media Analytics

likes=int(input("likes : "))
Comments=int(input("comments : "))
Shares=int(input("shares :"))
followers=int(input("follwers :"))
Reach=int(input("Reach :"))

Engagement_rate= (likes + Comments + Shares ) / followers * 100
print("Engagement Rate : ",Engagement_rate)

viral_score = ( Shares / Reach ) * 100
print("Viral Score : ",viral_score)



# Assignment – 15
# Company Profit Analysis

Revenue=int(input("enter revenue : "))
Expense=
Profit=


