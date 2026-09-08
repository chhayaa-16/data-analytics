# # #Student Performance Analyzer scenario
# #que 1 

# # print("Student academic performance")

# # number_of_sub=5
# # Name=input("Enter Student Name  : ")

# # print("SCORE CARD")

# # python=int(input("Enter Python marks  : "))
# # sql=int(input("Enter SQL marks : "))
# # excel=int(input("Enter EXCEL marks : "))
# # stat=int(input("Enter Statistics marks : "))
# # power_bi=int(input("Enter POWER BI marks : "))



# # total_marks = python + sql + excel + stat + power_bi
# # print("total Marks   :  ",total_marks)

# # per = (total_marks/500)*100
# # print("percentage  : ",per)


# # if python >= 35 and sql >= 35 and excel >= 35 and stat >= 35 and power_bi >= 35:
# #     print(" Status   :  PASS")
# # else:
# #     print(" Status   :  FAIL")



# # if per <= 95:
# #     print(" Grade A+")
# # elif per <= 90:
# #     print("A")
# # elif per <=70:
# #     print("B")
# # elif per <= 60:
# #     print("C")
# # else:
# #     ("Grade : FAIL")



# #  Employee Salary Analytics


# # E_Name=input("Employee Name  :  ")
# # Basic_Salary=int(input("Sallary in month : "))
# # HRA=int(input("HRA : "))
# # DA=int(input("DA : "))
# # Tax=int(input("TAX : "))
# # Bonus=int(input("Bonus : "))



# # Gross_salary= Basic_Salary + HRA + DA
# # print("Gross Salary :  ",Gross_salary)

# # Net_salary= Gross_salary - Tax 
# # print("Net Salary : ",Net_salary)

# # annual_salary= Basic_Salary * 12
# # print("Annual Salary : ", annual_salary)


# # if annual_salary <= 800000:
# #     print("Eligible for Bonus")
# # else:
# #      print("Not Eligible for Bonus")



# # --------------Assignment – 03
# #Product Sales Dashboard

# # Product_Name = input("Enter product Name : ")
# # Product_Price =int(input("Enetr product price : "))
# # Quantity_Sold = int(input("Enter Quantity sold : "))
# # GST = int(input("GST in %   : "))
# # Discount = int(input("Discount in %  : "))

# # # gross_sale = Quantity_Sold * Product_Price
# # # print ("Goss sale : ",gross_sale)

# # # GST_Amount=(Product_Price * GST) / 100
# # # print ("GST Amount : ",GST_Amount)

# # # Discount_amount=(Product_Price * Discount) / 100
# # # print ("GST Amount : ",Discount_amount)

# # # Final_Revenue= (gross_sale - Discount_amount) + GST_Amount
# # # print ("Final_Revenue: ",Final_Revenue)


# # # if Final_Revenue >= 50000:
# # #     print(f"{Product_Name} is a Top performer ")
# # # else:
# # #     print("no")


# # # Assignment – 04
# # # Customer Purchase Analysis

# # C_Name=input("Enter customer Name : " )
# # Purchase_Amount=int(input("Enter Purchase amount : "))
# # Membership= input("Membership (Yes/No): ")
# # Coupon_Applied= input("Coupon (Yes/No): ")

# # discount = 0

# # if member=="Yes":
# #     discount += purchase*0.10

# # if coupon=="Yes":
# #     discount += purchase*0.05

# # amount = purchase-discount
# # gst = amount*0.18
# # bill = amount+gst

# # print("Final Bill:", bill)

# # if bill>10000:
# #     print("Premium Customer")
# # else:
# #     print("Regular Customer")


# # #Que-----5
# # #Sales Executive KPI Analysis    

# # name = input("Executive Name: ")

# # target = int(input("Target: "))
# # sales = int(input("Actual Sales: "))
# # rating = float(input("Customer Rating: "))

# # achievement = sales/target*100

# # print("Achievement:",achievement,"%")

# # if achievement>=100:
# #     incentive=10000
# # else:
# #     incentive=5000

# # print("Incentive:",incentive)

# # if achievement>=100 and rating>=4:
# #     print("Promotion Eligible")
# # else:
# #     print("Not Eligible")


# # #Assignment – 06
# # #Attendance Analytics


# # name=input("Student Name: ")

# # total=int(input("Total Classes: "))
# # attended=int(input("Attended Classes: "))

# # percent=attended/total*100

# # print("Attendance:",percent)

# # if percent>=75:
# #     print("Eligible for Exam")
# # else:
# #     print("Not Eligible")

# # if percent>=90:
# #     print("Grade A")
# # elif percent>=75:
# #     print("Grade B")
# # else:
# #     print("Grade C")





# # Assignment – 07
# # Electricity Consumption Analysis


# # name=input("Consumer Name: ")

# # previous=int(input("Previous Reading: "))
# # current=int(input("Current Reading: "))
# # rate=float(input("Rate per Unit: "))

# # units=current-previous
# # bill=units*rate
# # gst=bill*0.18
# # final=bill+gst

# # print("Units:",units)
# # print("Final Bill:",final)

# # if units>500:
# #     print("High Consumption Alert ")
# # else:
# #     print("Normal")


# # Assignment – 08
# # Loan Eligibility Analyzer



# # name=input("Name: ")

# # age=int(input("Age: "))
# # salary=int(input("Monthly Salary: "))
# # emi=int(input("Existing EMI: "))
# # cibil=int(input("CIBIL Score: "))

# # ratio=emi/salary*100

# # print("EMI Ratio:",ratio)

# # if cibil>=750 and ratio<40:
# #     print("Loan Approved")
# # else:
# #     print("Loan Rejected")



# # Assignment – 09
# # Inventory Analytics

# # product=input("Product Name: ")

# # opening_stock=int(input("Opening Stock: "))
# # purchase=int(input("Purchased Stock: "))
# # sold=int(input("Sold Stock: "))

# # closing_stock=opening_stock+purchase-sold

# # print("Closing Stock:",closing_stock)
# # if closing<20:
# #     print("Reorder Required")
# # else:
# #     print("Stock Available")



# #     name=input("Patient Name: ")

# # weight=float(input("Weight: "))
# # height=float(input("Height in Meter: "))

# # bmi=weight/(height*height)

# # print("BMI:",bmi)

# # if bmi<18.5:
# #     print("Underweight")
# # elif bmi<25:
# #     print("Normal")
# # else:
# #     print("Overweight")


# # Assignment – 10
# # Hospital Patient Analytics


# # p_name=input("Enter patient name : ")
# # Age=int(input("Enter Age :" ))
# # Weight=int(input("Enter Weight :" ))
# # Sugar_level=int(input("Enter sugar Level :" ))
# # BP=int(input("Enter BP :" ))




# #Assignment – 11
# #Bank Transaction Analyzer

# print("BANK TRANSACTION ANALYZER")

# deposit = float(input("Enter deposit amount: "))
# withdrawal = float(input("Enter withdrawal amount: "))
# balance = deposit - withdrawal

# print("Balance:", balance)

# minimum_balance = 1000

# if balance >= minimum_balance:
#     print("Minimum Balance Check: Passed")
# else:
#     print("Minimum Balance Check: Failed")

# if withdrawal > 50000:
#     print("Fraud Alert: Large withdrawal detected")
# else:
#     print("Fraud Alert: No fraud detected")


# # Assignment – 12
# # Data Cleaning Report
# # Tasks
# # Missing Records.
# # Duplicate Records.
# # Clean Percentage.
# # Dataset Quality Score.
# # Ready for Analysis?



# print("DATA CLEANING REPORT")

# total_records = int(input("Enter total records: "))
# missing_records = int(input("Enter missing records: "))
# duplicate_records = int(input("Enter duplicate records: "))

# clean_records = total_records - missing_records - duplicate_records

# clean_percentage = (clean_records / total_records) * 100

# quality_score = clean_percentage

# print("Missing Records:", missing_records)
# print("Duplicate Records:", duplicate_records)
# print("Clean Percentage:", clean_percentage, "%")
# print("Dataset Quality Score:", quality_score)

# if quality_score >= 80:
#     print("Ready for Analysis: Yes")
# else:
#     print("Ready for Analysis: No")


# # Assignment – 13
# # Website Analytics
# # Tasks
# # Visitors.
# # Bounce Rate.
# # Conversion Rate.
# # Revenue.
# # Website Health




# print("WEBSITE ANALYTICS")

# visitors = int(input("Enter number of visitors: "))
# bounce_rate = float(input("Enter bounce rate (%): "))
# conversions = int(input("Enter number of conversions: "))
# revenue = float(input("Enter revenue: "))

# conversion_rate = (conversions / visitors) * 100

# print("Visitors:", visitors)
# print("Bounce Rate:", bounce_rate)
# print("Conversion Rate:", conversion_rate)
# print("Revenue: ", revenue)

# if bounce_rate <= 50 and conversion_rate >= 2:
#     print("Website Health: Good")
# else:
#     print("Website Health: Needs Improvement")








# # Assignment – 14
# # Social Media Analytics


# likes=int(input("likes : "))
# Comments=int(input("comments : "))
# Shares=int(input("shares :"))
# followers=int(input("follwers :"))
# Reach=int(input("Reach :"))

# Engagement_rate= (likes + Comments + Shares ) / followers * 100
# print("Engagement Rate : ",Engagement_rate)

# viral_score = ( Shares / Reach ) * 100
# print("Viral Score : ",viral_score)



# # Assignment – 15
# # Company Profit Analysis
# # Tasks
# # Revenue.
# # Expense.
# # Profit.
# # Profit Margin.
# # Growth Category.

# print("COMPANY PROFIT ANALYSIS")

# revenue = float(input("Enter revenue: "))
# expense = float(input("Enter expense: "))

# profit = revenue - expense
# profit_margin = (profit / revenue) * 100

# print("Revenue:", revenue)
# print("Expense:", expense)
# print("Profit:", profit)
# print("Profit Margin:", profit_margin,)

# if profit_margin >= 20:
#     print("Growth Category: High")
# elif profit_margin >= 10:
#     print("Growth Category: Medium")
# else:
#     print("Growth Category: Low")



# # Assignment – 16
# # Retail Store Dashboard
# # Tasks
# # Sales.
# # Discount.
# # GST.
# # Profit.
# # Best Selling Category.



# print("RETAIL STORE DASHBOARD")

# sales = float(input("Enter sales: "))
# discount = float(input("Enter discount: "))
# gst = float(input("Enter GST: "))
# cost = float(input("Enter product cost: "))

# discount_amount = sales * discount / 100
# gst_amount = (sales - discount_amount) * gst / 100
# profit = sales - discount_amount - cost

# print("Sales:", sales)
# print("Discount Amount:", discount_amount)
# print("GST Amount:", gst_amount)
# print("Profit:", profit)

# category = input("Enter best selling category: ")
# print("Best Selling Category:", category)



# # Assignment – 17
# # HR Performance Analytics
# # Tasks
# # Attendance.
# # Productivity.
# # Overtime.
# # Performance Rating.
# # Promotion Decision.



# print("HR PERFORMANCE ANALYTICS")

# attendance = float(input("Enter attendance percentage: "))
# productivity = float(input("Enter productivity percentage: "))
# overtime = float(input("Enter overtime hours: "))
# rating = float(input("Enter performance rating out of 10: "))

# print("Attendance:", attendance, "%")
# print("Productivity:", productivity, "%")
# print("Overtime:", overtime, "hours")
# print("Performance Rating:", rating)

# if attendance >= 90 and productivity >= 80 and rating >= 8:
#     print("Promotion Decision: Recommended")
# else:
#     print("Promotion Decision: Not Recommended")




# # Assignment – 18
# # University Admission Analytics
# # Tasks
# # Percentage.
# # Entrance Score.
# # Reservation.
# # Seat Availability.
# # Admission Status.


# print("UNIVERSITY ADMISSION ANALYTICS")

# percentage = float(input("Enter percentage: "))
# entrance_score = float(input("Enter entrance score: "))
# reservation = input("Enter reservation category: ")
# seats = int(input("Enter available seats: "))

# print("Percentage:", percentage)
# print("Entrance Score:", entrance_score)
# print("Reservation:", reservation)
# print("Available Seats:", seats)

# if percentage >= 60 and entrance_score >= 50 and seats > 0:
#     print("Admission Status: Eligible")
# else:
#     print("Admission Status: Not Eligible")


# # Assignment – 19
# # Insurance Premium Analytics
# # Tasks
# # Age Factor.
# # Health Score.
# # Premium.
# # Risk Level.
# # Approval.


# print("INSURANCE PREMIUM ANALYTICS")

# age = int(input("Enter age: "))
# health_score = int(input("Enter health score out of 100: "))

# if age < 30:
#     age_factor = 1
# elif age < 50:
#     age_factor = 1.5
# else:
#     age_factor = 2

# premium = 10000 * age_factor

# print("Age Factor:", age_factor)
# print("Health Score:", health_score)
# print("Premium:", premium)

# if health_score >= 80:
#     print("Risk Level: Low")
#     print("Approval: Approved")
# elif health_score >= 60:
#     print("Risk Level: Medium")
#     print("Approval: Approved")
# else:
#     print("Risk Level: High")
#     print("Approval: Not Approved")


# #  Assignment – 20
# # E-Commerce Dashboard
# # Tasks
# # Cart Value.
# # Shipping.
# # Coupon.
# # GST.
# # Final Bill.


# print("E-COMMERCE DASHBOARD")

# cart_value = float(input("Enter cart value: "))
# shipping = float(input("Enter shipping charge: "))
# coupon = float(input("Enter coupon discount: "))
# gst = float(input("Enter GST percentage: "))

# after_coupon = cart_value - coupon
# gst_amount = after_coupon * gst / 100
# final_bill = after_coupon + shipping + gst_amount

# print("Cart Value:", cart_value)
# print("Shipping:", shipping)
# print("Coupon Discount:", coupon)
# print("GST:", gst_amount)
# print("Final Bill:", final_bill)

# # Assignment – 21
# # Restaurant Sales Analytics
# # Tasks
# # Food Bill.
# # GST.
# # Service Charge.
# # Discount.
# # Final Invoice.


# print("RESTAURANT SALES ANALYTICS")

# food_bill = float(input("Enter food bill: "))
# gst = float(input("Enter GST percentage: "))
# service_charge = float(input("Enter service charge percentage: "))
# discount = float(input("Enter discount percentage: "))

# discount_amount = food_bill * discount / 100
# after_discount = food_bill - discount_amount

# gst_amount = after_discount * gst / 100
# service_amount = after_discount * service_charge / 100

# final_invoice = after_discount + gst_amount + service_amount

# print("Food Bill:", food_bill)
# print("GST Amount:", gst_amount)
# print("Service Charge:", service_amount)
# print("Discount:", discount_amount)
# print("Final Invoice:", final_invoice)

# #
# # 
# # 
# # 
# #  Assignment – 22
# # Weather Data Analytics
# # Tasks
# # Average Temperature.
# # Rainfall Category.
# # Humidity Level.
# # Climate Score.
# # Alert.


# print("WEATHER DATA ANALYTICS")

# temperature = float(input("Enter temperature: "))
# rainfall = float(input("Enter rainfall in mm: "))
# humidity = float(input("Enter humidity percentage: "))

# print("Average Temperature:", temperature)

# if rainfall < 50:
#     print("Rainfall Category: Low")
# elif rainfall < 100:
#     print("Rainfall Category: Medium")
# else:
#     print("Rainfall Category: High")

# if humidity < 40:
#     print("Humidity Level: Low")
# elif humidity < 70:
#     print("Humidity Level: Medium")
# else:
#     print("Humidity Level: High")

# climate_score = 100 - humidity

# print("Climate Score:", climate_score)

# if temperature > 40 or rainfall > 150:
#     print("Alert: Extreme Weather")
# else:
#     print("Alert: Normal")



# # Assignment – 23
# # Manufacturing Analytics
# # Tasks
# # Production.
# # Defective Units.
# # Efficiency.
# # Quality Score.
# # Production Status.



# print("MANUFACTURING ANALYTICS")

# production = int(input("Enter total production units: "))
# defective = int(input("Enter defective units: "))

# good_units = production - defective
# efficiency = (good_units / production) * 100
# quality_score = (good_units / production) * 100

# print("Production:", production)
# print("Defective Units:", defective)
# print("Efficiency:", efficiency, "%")
# print("Quality Score:", quality_score)

# if efficiency >= 90:
#     print("Production Status: Good")
# else:
#     print("Production Status: Needs Improvement")




# # Assignment – 24
# # Stock Market Analytics
# # Tasks
# # Buy Price.
# # Sell Price.
# # Profit/Loss.
# # ROI.
# # Investment Recommendation.


# print("STOCK MARKET ANALYTICS")

# buy_price = float(input("Enter buy price: "))
# sell_price = float(input("Enter sell price: "))
# investment = float(input("Enter investment amount: "))

# profit_loss = sell_price - buy_price
# roi = (profit_loss / buy_price) * 100

# print("Buy Price:", buy_price)
# print("Sell Price:", sell_price)

# if profit_loss > 0:
#     print("Profit:", profit_loss)
# else:
#     print("Loss:", abs(profit_loss))

# print("ROI:", roi, "%")

# if roi >= 10:
#     print("Investment Recommendation: Buy")
# elif roi > 0:
#     print("Investment Recommendation: Hold")
# else:
#     print("Investment Recommendation: Avoid")





# # Assignment – 25
# # Cyber Security Log Analytics
# # Tasks
# # Failed Logins.
# # Successful Logins.
# # Suspicious Activity.
# # Risk Score.
# # Security Status.


# print("CYBER SECURITY LOG ANALYTICS")

# failed = int(input("Enter failed logins: "))
# successful = int(input("Enter successful logins: "))
# suspicious = int(input("Enter suspicious activities: "))

# risk_score = failed + (suspicious * 10)

# print("Failed Logins:", failed)
# print("Successful Logins:", successful)
# print("Suspicious Activity:", suspicious)
# print("Risk Score:", risk_score)

# if risk_score >= 50:
#     print("Security Status: High Risk")
# elif risk_score >= 20:
#     print("Security Status: Medium Risk")
# else:
#     print("Security Status: Safe")



# # Assignment – 26
# # Call Center Analytics
# # Tasks
# # Calls Received.
# # Calls Resolved.
# # Average Handling Time.
# # Resolution Rate.
# # Employee Rating.



# print("CALL CENTER ANALYTICS")

# calls_received = int(input("Enter calls received: "))
# calls_resolved = int(input("Enter calls resolved: "))
# handling_time = float(input("Enter average handling time in minutes: "))

# resolution_rate = (calls_resolved / calls_received) * 100

# print("Calls Received:", calls_received)
# print("Calls Resolved:", calls_resolved)
# print("Average Handling Time:", handling_time, "minutes")
# print("Resolution Rate:", resolution_rate, "%")

# if resolution_rate >= 90:
#     print("Employee Rating: Excellent")
# elif resolution_rate >= 70:
#     print("Employee Rating: Good")
# else:
#     print("Employee Rating: Needs Improvement")





# # Assignment – 27
# # Fuel Consumption Analytics
# # Tasks
# # Distance.
# # Fuel Used.
# # Mileage.
# # Fuel Cost.
# # Efficiency Rating.




# print("FUEL CONSUMPTION ANALYTICS")

# distance = float(input("Enter distance in km: "))
# fuel_used = float(input("Enter fuel used in litres: "))
# fuel_price = float(input("Enter fuel price per litre: "))

# mileage = distance / fuel_used
# fuel_cost = fuel_used * fuel_price

# print("Distance:", distance, "km")
# print("Fuel Used:", fuel_used, "litres")
# print("Mileage:", mileage, "km/litre")
# print("Fuel Cost:", fuel_cost)

# if mileage >= 20:
#     print("Efficiency Rating: Excellent")
# elif mileage >= 15:
#     print("Efficiency Rating: Good")
# else:
#     print("Efficiency Rating: Low")


# # Assignment – 28
# # Airline Booking Analytics
# # Tasks
# # Ticket Price.
# # Tax.
# # Baggage Charge.
# # Final Fare.
# # Seat Upgrade Eligibility.


# print("AIRLINE BOOKING ANALYTICS")

# ticket_price = float(input("Enter ticket price: "))
# tax = float(input("Enter tax percentage: "))
# baggage = float(input("Enter baggage charge: "))

# tax_amount = ticket_price * tax / 100
# final_fare = ticket_price + tax_amount + baggage

# print("Ticket Price:", ticket_price)
# print("Tax:", tax_amount)
# print("Baggage Charge:", baggage)
# print("Final Fare:", final_fare)

# if ticket_price >= 10000:
#     print("Seat Upgrade Eligibility: Eligible")
# else:
#     print("Seat Upgrade Eligibility: Not Eligible")


# # Assignment – 29
# # Smart City Traffic Analytics
# # Tasks
# # Vehicle Count.
# # Average Speed.
# # Congestion Level.
# # Traffic Score.
# # Alert Status.


# print("SMART CITY TRAFFIC ANALYTICS")

# vehicles = int(input("Enter vehicle count: "))
# speed = float(input("Enter average speed: "))

# print("Vehicle Count:", vehicles)
# print("Average Speed:", speed, "km/h")

# if vehicles > 1000 and speed < 30:
#     congestion = "High"
# elif vehicles > 500 and speed < 50:
#     congestion = "Medium"
# else:
#     congestion = "Low"

# traffic_score = speed

# print("Congestion Level:", congestion)
# print("Traffic Score:", traffic_score)

# if congestion == "High":
#     print("Alert Status: Traffic Alert")
# else:
#     print("Alert Status: Normal")


# # Assignment – 30
# # Data Analytics KPI Dashboard (Capstone Project)
# # Scenario

# # You are a Junior Data Analyst in a company. Build a console-based KPI dashboard using user inputs.

# # Accept Input
# # Company Name
# # Total Employees
# # Total Revenue
# # Total Expenses
# # New Customers
# # Existing Customers
# # Monthly Sales
# # Customer Satisfaction Score
# # Employee Attendance %
# # Project Completion %
# # Tasks
# # Calculate Net Profit and Profit Margin (%).
# # Calculate Customer Growth Rate and classify it as Low, Medium, or High.
# # Determine Business Health using nested if and logical operators (Profit Margin, Customer Satisfaction, and Attendance).
# # Display Executive Dashboard Summary showing all calculated KPIs in a formatted report.
# # Generate a final recommendation:
# # Excellent Performance
# # Good Performance
# # Needs Improvement
# # Critical Attention Required





# print("DATA ANALYTICS KPI DASHBOARD")


# company_name = input("Enter company name: ")
# employees = int(input("Enter total employees: "))
# revenue = float(input("Enter total revenue: "))
# expenses = float(input("Enter total expenses: "))
# new_customers = int(input("Enter new customers: "))
# existing_customers = int(input("Enter existing customers: "))
# monthly_sales = float(input("Enter monthly sales: "))
# satisfaction = float(input("Enter customer satisfaction score: "))
# attendance = float(input("Enter employee attendance %: "))
# completion = float(input("Enter project completion %: "))


# net_profit = revenue - expenses
# profit_margin = (net_profit / revenue) * 100


# customer_growth = (new_customers / existing_customers) * 100

# if customer_growth < 10:
#     growth_category = "Low"
# elif customer_growth < 25:
#     growth_category = "Medium"
# else:
#     growth_category = "High"


# if profit_margin >= 20 and satisfaction >= 80 and attendance >= 90:
#     business_health = "Excellent"
# elif profit_margin >= 10 and satisfaction >= 60 and attendance >= 75:
#     business_health = "Good"
# else:
#     business_health = "Poor"


# if business_health == "Excellent" and completion >= 90:
#     recommendation = "Excellent Performance"
# elif business_health == "Good" and completion >= 70:
#     recommendation = "Good Performance"
# elif business_health == "Poor" and completion < 50:
#     recommendation = "Critical Attention Required"
# else:
#     recommendation = "Needs Improvement"

# print("EXECUTIVE DASHBOARD")


# print("Company Name:", company_name)
# print("Total Employees:", employees)
# print("Total Revenue:", revenue)
# print("Total Expenses:", expenses)
# print("Net Profit:", net_profit)
# print("Profit Margin:", profit_margin, "%")
# print("New Customers:", new_customers)
# print("Existing Customers:", existing_customers)
# print("Customer Growth Rate:", customer_growth, "%")
# print("Growth Category:", growth_category)
# print("Monthly Sales:", monthly_sales)
# print("Customer Satisfaction:", satisfaction)
# print("Employee Attendance:", attendance, "%")
# print("Project Completion:", completion, "%")
# print("Business Health:", business_health)

# print("FINAL RECOMMENDATION:", recommendation)
