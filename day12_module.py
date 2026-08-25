####  Questions based on modules top 20 practice questions 
# second file ----emain.py


# 1. Student Management System

# Create a user-defined module to manage student information.

# Tasks
# Accept details of 10 students using user input.
# Calculate total, percentage, and grade using module functions.
# Create a Student class to store and display details.
# Find the topper and lowest scorer.
# Display class average percentage.
# Save all student details in another module and display them.



# def total_marks(marks):
#     return sum(marks)


# def percentage(total):
#     return total / 5


# def grade(per):
#     if per >= 90:
#         return "A+"
#     elif per >= 80:
#         return "A"
#     elif per >= 70:
#         return "B"
#     elif per >= 60:
#         return "C"
#     elif per >= 50:
#         return "D"
#     else:
#         return "Fail"


# students = []


# class Student:

#     def __init__(self, roll, name, marks, total, percentage, grade):
#         self.roll = roll
#         self.name = name
#         self.marks = marks
#         self.total = total
#         self.percentage = percentage
#         self.grade = grade

#     def display(self):
        
#         print("Roll No :", self.roll)
#         print("Name :", self.name)
#         print("Marks :", self.marks)
#         print("Total :", self.total)
#         print("Percentage :", self.percentage)
#         print("Grade :", self.grade)






# 2. Employee Payroll System

# Create a payroll management module.

# Tasks
# Accept employee details using user input.
# Calculate HRA, DA, PF, and Net Salary.
# Create an Employee class.
# Display the highest-paid employee.
# Count employees whose salary is above ₹50,000.
# Generate a payroll report using imported modules.




# employees = []


# def calculate_hra(basic):
#     return basic * 20 / 100


# def calculate_da(basic):
#     return basic * 10 / 100


# def calculate_pf(basic):
#     return basic * 12 / 100


# def calculate_net_salary(basic):

#     hra = calculate_hra(basic)
#     da = calculate_da(basic)
#     pf = calculate_pf(basic)

#     gross = basic + hra + da
#     net = gross - pf

#     return hra, da, pf, net


# class Employee:

#     def __init__(self, emp_id, name, basic, hra, da, pf, net):

#         self.emp_id = emp_id
#         self.name = name
#         self.basic = basic
#         self.hra = hra
#         self.da = da
#         self.pf = pf
#         self.net = net

#     def display(self):

#         print("Employee ID :", self.emp_id)
#         print("Name :", self.name)
#         print("Basic Salary :", self.basic)
#         print("HRA :", self.hra)
#         print("DA :", self.da)
#         print("PF :", self.pf)
#         print("Net Salary :", self.net)







# que 3 

# 3. Library Management System

# Design a library system using user-defined modules.

# Tasks
# Add books using user input.
# Create a Book class.
# Issue and return books using module functions.
# Count available and issued books.
# Search books by title or author.

# books = []


# class Book:

#     def __init__(self, book_id, title, author):

#         self.book_id = book_id
#         self.title = title
#         self.author = author
#         self.status = "Available"


#     def display(self):

#         print("Book ID :", self.book_id)
#         print("Title :", self.title)
#         print("Author :", self.author)
#         print("Status :", self.status)


# def issue_book(book_id):

#     for book in books:

#         if book.book_id == book_id:

#             if book.status == "Available":

#                 book.status = "Issued"

#                 return True

#             else:

#                 return False

#     return False


# def return_book(book_id):

#     for book in books:

#         if book.book_id == book_id:

#             if book.status == "Issued":

#                 book.status = "Available"

#                 return True

#             else:

#                 return False

#     return False


# def count_available():

#     count = 0

#     for book in books:

#         if book.status == "Available":

#             count += 1

#     return count


# def count_issued():

#     count = 0

#     for book in books:

#         if book.status == "Issued":

#             count += 1

#     return count


# def search_book(search_text):

#     result = []

#     for book in books:

#         if (search_text.lower() in book.title.lower() or
#                 search_text.lower() in book.author.lower()):

#             result.append(book)

#     return result




# 4. Banking System

# Develop a banking application.

# Tasks
# Create an Account class.
# Perform Deposit, Withdrawal, and Balance Inquiry.
# Maintain transaction history.
# Calculate yearly interest.
# Display the customer with the highest balance.
# Generate an account summary report.

# accounts = []


# class Account:

#     def __init__(self, account_no, name, balance):

#         self.account_no = account_no
#         self.name = name
#         self.balance = balance
#         self.transactions = []

#     def deposit(self, amount):

#         self.balance += amount

#         self.transactions.append(
#             "Deposited : " + str(amount)
#         )

#     def withdraw(self, amount):

#         if amount <= self.balance:

#             self.balance -= amount

#             self.transactions.append(
#                 "Withdrawn : " + str(amount)
#             )

#             return True

#         else:

#             return False

#     def balance_inquiry(self):

#         return self.balance

#     def yearly_interest(self, rate):

#         interest = self.balance * rate / 100

#         return interest

#     def display(self):

        
#         print("Account Number :", self.account_no)
#         print("Customer Name :", self.name)
#         print("Balance :", self.balance)


#         for transaction in self.transactions:

#             print(transaction)




# 5. Hospital Management System

# Create hospital management modules.

# Tasks
# Register patients using user input.
# Create Patient and Doctor classes.
# Calculate total treatment cost.
# Display admitted and discharged patients.
# Find the patient with the highest bill.
# Print the hospital report.





# ============================================================
# QUESTION 5 - HOSPITAL MANAGEMENT SYSTEM
# ============================================================

patients = []


class Patient:

    def __init__(self, patient_id, name, age, doctor, treatment_cost):

        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.doctor = doctor
        self.treatment_cost = treatment_cost
        self.status = "Admitted"


    def display(self):

        print("----------------------------")
        print("Patient ID :", self.patient_id)
        print("Patient Name :", self.name)
        print("Age :", self.age)
        print("Doctor :", self.doctor.name)
        print("Treatment Cost :", self.treatment_cost)
        print("Status :", self.status)


class Doctor:

    def __init__(self, doctor_id, name, specialization):

        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization


    def display(self):

        print("----------------------------")
        print("Doctor ID :", self.doctor_id)
        print("Doctor Name :", self.name)
        print("Specialization :", self.specialization)


def calculate_treatment_cost(consultation, medicine, room):

    total = consultation + medicine + room

    return total


def discharge_patient(patient_id):

    for patient in patients:

        if patient.patient_id == patient_id:

            patient.status = "Discharged"

            return True

    return False