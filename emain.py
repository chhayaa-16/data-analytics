# # import employee 


# # basic = int(input("enter salary :  "))


# # final_salary = employee.calculate_salary(basic)
# # print(final_salary)

# # total = employee.calculate_salary(basic)
# # print(total)


# # e_id = int(input("Enter Employee Id : "))
# # e_name = input("Enter Employee Name : ")

# # # create object for class

# # emp1 = employee.Employee(e_id,e_name,final_salary)
# # emp1.show()



# import employee

# basic = int(input("enter salary : "))

# final_salary = employee.calculate_salary(basic)
# print(final_salary)

# total = employee.calculate_salary(basic)
# print(total)

# # e_id = int(input("Enter Employee Id : "))
# # e_name = input("Enter Employee Name : ")


# # emp1 = employee.Employee(e_id, e_name, final_salary)
# # emp1.show()




# ######## asignment questions --- module second file  


# # que one 

# # import day12_module


# # for i in range(10):

# #     print("\nEnter Details of Student", i + 1)

# #     roll = int(input("Enter Roll Number : "))
# #     name = input("Enter Name : ")

# #     marks = []

# #     for j in range(5):
# #         m = int(input(f"Enter Subject {j+1} Marks : "))
# #         marks.append(m)

# #     total = day12_module.total_marks(marks)
# #     per = day12_module.percentage(total)
# #     g = day12_module.grade(per)

# #     s = day12_module.Student(roll, name, marks, total, per, g)

# #     day12_module.students.append(s)


# # for s in day12_module.students:
# #     s.display()




# # topper = day12_module.students[0]

# # for s in day12_module.students:
# #     if s.percentage > topper.percentage:
# #         topper = s


# # topper.display()


# # lowest = day12_module.students[0]

# # for s in day12_module.students:
# #     if s.percentage < lowest.percentage:
# #         lowest = s


# # lowest.display()


# # total_per = 0

# # for s in day12_module.students:
# #     total_per += s.percentage

# # avg = total_per / len(day12_module.students)

# # print("\nClass Average Percentage :", avg)



# # for s in day12_module.students:
# #     s.display()





# #        que 2 

# # 2. Employee Payroll System



# import day12_module


# for i in range(5):

#     print("\nEnter Employee", i + 1)

#     emp_id = int(input("Enter Employee ID : "))
#     name = input("Enter Name : ")
#     basic = float(input("Enter Basic Salary : "))

#     hra, da, pf, net = day12_module.calculate_net_salary(basic)

#     emp = day12_module.Employee(
#         emp_id,
#         name,
#         basic,
#         hra,
#         da,
#         pf,
#         net
#     )

#     day12_module.employees.append(emp)



# for emp in day12_module.employees:

#     emp.display()


# highest = day12_module.employees[0]


# for emp in day12_module.employees:

#     if emp.net > highest.net:
#         highest = emp




# highest.display()


# count = 0


# for emp in day12_module.employees:

#     if emp.net > 50000:
#         count += 1


# print("\nEmployees having Net Salary above ₹50,000 :", count)



### que 3 


# import day12_module
# for i in range(5):

#     print("\nEnter Book", i + 1)

#     book_id = int(input("Enter Book ID : "))
#     title = input("Enter Book Title : ")
#     author = input("Enter Author Name : ")

#     bookss = day12_module.Book(
#         book_id,
#         title,
#         author
#     )

#     day12_module.books.append(bookss)




# for book in day12_module.books:

#     book.display()


# issue_id = int(input("\nEnter Book ID to Issue : "))

# result = day12_module.issue_book(issue_id)


# if result:

#     print("Book issued successfully.")

# else:

#     print("Book cannot be issued.")





# return_id = int(input("\nEnter Book ID to Return : "))

# result = day12_module.return_book(return_id)


# if result:

#     print("Book returned successfully.")

# else:

#     print("Book cannot be returned.")





# search_book = input("\nEnter Book Title or Author to Search : ")

# result = day12_module.search_book(search_book)




# if len(result) == 0:

#     print("Book not found.")

# else:

#     for book in result:

#         book.display()





# available = day12_module.count_available()

# issued = day12_module.count_issued()



# print("Available Books :", available)

# print("Issued Books :", issued)




# for book in day12_module.books:

#     book.display()



##### quee ---4 


# import day12_module

# # for i in range(5):

# #     print("\nEnter Customer", i + 1)

# #     account_no = int(input("Enter Account Number : "))
# #     name = input("Enter Customer Name : ")
# #     balance = float(input("Enter Opening Balance : "))

# #     account = day12_module.Account(
# #         account_no,
# #         name,
# #         balance
# #     )

# #     day12_module.accounts.append(account)



# # deposit_no = int(input("Enter Account Number for Deposit : "))
# # deposit_amount = int(input("Enter Deposit Amount : "))


# # for account in day12_module.accounts:

# #     if account.account_no == deposit_no:

# #         account.deposit(deposit_amount)

# #         print("Amount deposit successfully.")



# # withdraw_no = int(input("Enter Account Number for Withdrawal : "))
# # withdraw_amount = int(input("Enter Withdrawal Amount : "))


# # for account in day12_module.accounts:

# #     if account.account_no == withdraw_no:

# #         result = account.withdraw(withdraw_amount)

# #         if result:

# #             print("Amount withdrawn successfully.")

# #         else:

# #             print("Insufficient balance.")


# # inquiry_no = int(input("Enter Account Number : "))


# # for account in day12_module.accounts:

# #     if account.account_no == inquiry_no:

# #         print("Customer Name :", account.name)
# #         print("Current Balance :", account.balance_inquiry())



# # interest_rate = float(input("Enter Interest Rate (%) : "))


# # for account in day12_module.accounts:

# #     interest = account.yearly_interest(interest_rate)

# #     print("\nAccount Number :", account.account_no)
# #     print("Customer Name :", account.name)
# #     print("Yearly Interest :", interest)



# # highest = day12_module.accounts[0]


# # for account in day12_module.accounts:

# #     if account.balance > highest.balance:

# #         highest = account



# # print("Account Number :", highest.account_no)
# # print("Customer Name :", highest.name)
# # print("Balance :", highest.balance)



# # for account in day12_module.accounts:

# #     account.display()





# #### que 5 


# import day12_module


# for i in range(5):

#     print("\nEnter Patient", i + 1)

#     patient_id = int(input("Enter Patient ID : "))
#     name = input("Enter Patient Name : ")
#     age = int(input("Enter Age : "))

#     print("\nEnter Doctor Details")

#     doctor_id = int(input("Enter Doctor ID : "))
#     doctor_name = input("Enter Doctor Name : ")
#     specialization = input("Enter Specialization : ")

#     doctor = day12_module.Doctor(
#         doctor_id,
#         doctor_name,
#         specialization
#     )

#     print("\nEnter Treatment Details")

#     consultation = float(
#         input("Enter Consultation Cost : ")
#     )

#     medicine = float(
#         input("Enter Medicine Cost : ")
#     )

#     room = float(
#         input("Enter Room Cost : ")
#     )

#     total = day12_module.calculate_treatment_cost(
#         consultation,
#         medicine,
#         room
#     )

#     patient = day12_module.Patient(
#         patient_id,
#         name,
#         age,
#         doctor,
#         total
#     )

#     day12_module.patients.append(patient)


# for patient in day12_module.patients:

#     patient.display()



# discharge_id = int(
#     input("Enter Patient ID to Discharge : ")
# )

# result = day12_module.discharge_patient(
#     discharge_id
# )


# if result:

#     print("Patient discharged successfully.")

# else:

#     print("Patient ID not found.")


# for patient in day12_module.patients:

#     if patient.status == "Admitted":

#         patient.display()



# for patient in day12_module.patients:

#     if patient.status == "Discharged":

#         patient.display()


# highest = day12_module.patients[0]


# for patient in day12_module.patients:

#     if patient.treatment_cost > highest.treatment_cost:

#         highest = patient



# print("Patient ID :", highest.patient_id)
# print("Patient Name :", highest.name)
# print("Treatment Cost :", highest.treatment_cost)



# for patient in day12_module.patients:

#     patient.display()






#======== asignment que=====10-8-26=========
# second file code    
# 20 MID-LEVEL PRACTICAL QUESTIONS
# NumPy + Matplotlib Numeric and Chart Operations



# que 1 



# import numpy as np
# import matplotlib.pyplot as plt

# from num_matQ import (
#     calculate_total,
#     calculate_average,
#     find_lowest_average,
#     calculate_grades,
#     sort_students,
#     find_unique_grades
# )


# number_of_students = int(
#     input("Enter number of students: ")
# )

# names = []
# marks_data = []


# for i in range(number_of_students):

#     print("\nEnter details for Student", i + 1)

#     name = input("Enter student name: ")

#     python = float(input("Enter Python marks: "))
#     sql = float(input("Enter SQL marks: "))
#     excel = float(input("Enter Excel marks: "))
#     statistics = float(input("Enter Statistics marks: "))
#     powerbi = float(input("Enter Power BI marks: "))

#     names.append(name)

#     marks_data.append([
#         python,
#         sql,
#         excel,
#         statistics,
#         powerbi
#     ])


# marks = np.array(marks_data)



# total = calculate_total(marks)

# average = calculate_average(marks)

# lowest_name, lowest_average = find_lowest_average(
#     names,
#     average
# )

# grades = calculate_grades(average)

# sorted_names, sorted_total = sort_students(
#     names,
#     total
# )

# unique_grades = find_unique_grades(grades)



# print("\n")

# print(" STUDENT PERFORMANCE ANALYSIS")


# for i in range(number_of_students):

#     print("Student Name :", names[i])
#     print("Total Marks :", total[i])
#     print("Average  :", average[i])
#     print("Grade :", grades[i])



# print("Student with Lowest Average")

# print("Student Name :", lowest_name)
# print("Average  :", lowest_average)



# print("Students Sorted According to Total Marks")

# for i in range(len(sorted_names)):

#     print(
#         sorted_names[i],
#         "->",
#         sorted_total[i]
#     )


# print("Unique Grades:")

# print(unique_grades)





# plt.figure(figsize=(8, 5))

# plt.bar(names, total)

# plt.xlabel("Students")
# plt.ylabel("Total Marks")

# plt.title("Student Total Marks")

# plt.xticks(rotation=45)

# plt.tight_layout()

# plt.show()


# # histogram


# plt.figure(figsize=(8, 5))

# plt.hist(average, bins=5)

# plt.xlabel("Average Marks")
# plt.ylabel("Number of Students")

# plt.title("Student Average Marks Distribution")

# plt.tight_layout()

# plt.show()


#============== que 2=====================

# import numpy as np
# import matplotlib.pyplot as plt

# from num_matQ import (
#     s_array,
#     anual_sale,
#     min_product,
#     reshape_sales,
#     uni_sales,
#     month_sales
# )



# products = []

# print("Enter names of 5 products:")

# for i in range(5):
#     product_name = input(f"Enter product {i + 1} name: ")
#     products.append(product_name)


# print("\nEnter sales data for 12 months")
# print("Enter sales for each product month by month.\n")

# sales_data = []

# for month in range(12):

#     print(f"Month {month + 1}")

#     monthly_data = []

#     for product in products:
#         sales = float(input(f"Enter sales for {product}: "))
#         monthly_data.append(sales)

#     sales_data.append(monthly_data)




# sales_array = s_array(sales_data)

# print("\nOriginal Sales Array:")
# print(sales_array)




# annual_sales = anual_sale(sales_array)

# print("\nAnnual Sales of Each Product:")

# for i in range(5):
#     print(f"{products[i]} : {annual_sales[i]:.2f}")




# min_index = min_product(annual_sales)

# print("\nProduct Having Minimum Annual Sales:")
# print(products[min_index])

# print(f"Minimum Annual Sales: "
#       f"{annual_sales[min_index]:.2f}")



# reshaped_data = reshape_sales(sales_array)

# print("\nReshaped Sales Data:")
# print(reshaped_data)


# unique_values = uni_sales(sales_array)

# print("\nUnique Sales Values:")
# print(unique_values)




# monthly_sales = month_sales(sales_array)

# print("\nTotal Sales for Each Month:")

# for i in range(12):
#     print(f"Month {i + 1}: {monthly_sales[i]:.2f}")



# months = np.arange(1, 13)

# plt.figure(figsize=(10, 6))

# for i in range(5):
#     plt.plot(
#         months,
#         sales_array[:, i],
#         marker='o',
#         label=products[i]
#     )

# plt.title("Monthly Sales of Products")
# plt.xlabel("Month")
# plt.ylabel("Sales")
# plt.xticks(months)
# plt.legend()
# plt.grid(True)

# plt.show()



# plt.figure(figsize=(10, 6))

# plt.bar(products, annual_sales)

# plt.title("Annual Sales of Products")
# plt.xlabel("Products")
# plt.ylabel("Total Annual Sales")

# plt.show()






# #############################################################################################################3
#  day 3 ----shreyas, chhaya ,shruti assignmment  named  second file 







