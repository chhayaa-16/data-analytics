# Question 1: Student Management System

# Create a Student class.

# Tasks
# Accept Student ID, Name, Age and Course.
# Create a method to display student details.
# Create a method to update the course.
# Create three student objects.
# Display all student information.

# Concepts: Class, Object, Constructor, Methods


class Student:

    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    def display_details(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


    
    def update_course(self, new_course):
        self.course = new_course



s1 = Student(1, "raj", 22, "Python")
s2 = Student(2, "Piyu", 19, "Java")
s3 = Student(3, "Arun", 24, "C++")



s1.display_details()
s2.display_details()
s3.display_details()



s1.update_course("Data Science")
s1.display_details()




# Question 2: Employee Salary Management

# Create an Employee class.

# Tasks
# Accept Employee Name, Department and Monthly Salary.
# Calculate Yearly Salary.
# Calculate 10% Bonus.
# Display complete employee details.
# Create data for five employees.

# Data Analytics Use Case: Employee Payroll Analysis





class Employee:

    
    def __init__(self, name, department, monthly_salary):
        self.name = name
        self.department = department
        self.monthly_salary = monthly_salary


    def cal_year_salary(self):
        return self.monthly_salary * 12



    def calculate_bonus(self):
        return self.monthly_salary * 12 * 0.10

    
    def display_details(self):
        print("Employee Name:", self.name)
        print("Department:", self.department)
        print("Monthly Salary:", self.monthly_salary)
        print("Yearly Salary:", self.cal_year_salary())
        print("10% Bonus:", self.calculate_bonus())
        print()



emp1 = Employee("Raj", "IT", 80000)
emp2 = Employee("Piyu", "HR", 87000)
emp3 = Employee("Arun", "Finance", 67000)
emp4 = Employee("Sejal", "Marketing", 37000)
emp5 = Employee("Rohan", "Sales", 32000)



emp1.display_details()
emp2.display_details()
emp3.display_details()
emp4.display_details()
emp5.display_details()






# Question 3: Bank Account System

# Create a BankAccount class.

# Tasks
# Accept Account Number, Account Holder Name and Balance.
# Create a Deposit method.
# Create a Withdraw method.
# Display updated balance.
# Create three bank account objects.




class BankAccount:

    
    def __init__(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    
    def deposit(self, amount):
        self.balance = self.balance + amount

    
    def withdraw(self, amount):
        self.balance = self.balance - amount

    
    def display_details(self):
        print("Account Number:", self.account_number)
        print("Account Holder Name:", self.account_holder_name)
        print("Balance:", self.balance)
        print()



a1 = BankAccount(1001, "Raj", 80000)
a2 = BankAccount(1002, "Piyu", 52000)
a3 = BankAccount(1003, "Arun", 28000)



a1.deposit(5000)
a2.deposit(3000)
a3.deposit(7000)

a1.withdraw(2000)
a2.withdraw(500)
a3.withdraw(3000)


a1.display_details()
a2.display_details()
a3.display_details()

# =======================Question 4: Sales Data Analyzer

# Create a SalesData class.

# Tasks
# Accept sales for 6 months.
# Calculate Total Sales.
# Calculate Average Sales.
# Find Maximum Sales.
# Find Minimum Sales.

# Data Analytics Project



class SalesData:

    
    def __init__(self, month1, month2, month3, month4, month5, month6):
        self.month1 = month1
        self.month2 = month2
        self.month3 = month3
        self.month4 = month4
        self.month5 = month5
        self.month6 = month6

    
    def calculate_total(self):
        return self.month1 + self.month2 + self.month3 + self.month4 + self.month5 + self.month6

    
    def calculate_average(self):
        return self.calculate_total() / 6

    def max(self):
        return max(self.month1, self.month2, self.month3, self.month4, self.month5, self.month6)

    
    def min(self):
        return min(self.month1, self.month2, self.month3, self.month4, self.month5, self.month6)

    
    def display_details(self):
        print("Month 1 Sales:", self.month1)
        print("Month 2 Sales:", self.month2)
        print("Month 3 Sales:", self.month3)
        print("Month 4 Sales:", self.month4)
        print("Month 5 Sales:", self.month5)
        print("Month 6 Sales:", self.month6)
        print("Total Sales:", self.calculate_total())
        print("Average Sales:", self.calculate_average())
        print("Maximum Sales:", self.find_maximum())
        print("Minimum Sales:", self.find_minimum())



sales = SalesData(10000, 15000, 12000, 18000, 20000, 16000)



sales.display_details()




# Question 5: Login Authentication System

# Create a LoginSystem class.

# Tasks
# Store Username and Password.
# Create a Login method.
# Display Login Status.
# Count Total Login Attempts.
# Display Login Report.

# Cyber Security Project



class LoginSystem:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.login_attempts = 0

    def Login(self, username, password):
        self.login_attempts += 1

        if username == self.username and password == self.password:
            print("Login Successful")
        else:
            print("Login Failed")

    def DisplayLoginStatus(self):
        print("Username:", self.username)
        print("Login Attempts:", self.login_attempts)

    def DisplayLoginReport(self):
        print("Login Report")
        print("Username:", self.username)
        print("Total Login Attempts:", self.login_attempts)



login = LoginSystem("admin", "1234")
login.Login("admin", "1234")
login.DisplayLoginStatus()
login.DisplayLoginReport()



# Question 6: Product Inventory Management

# Create a Product class.

# Tasks
# Add Product Details.
# Update Product Quantity.
# Search Product by Name.
# Display Product Information.
# Create five product objects.



class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def AddProductDetails(self):
        print("Product Added")
        print("Name:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)

    def UpdateProductQuantity(self, quantity):
        self.quantity = quantity
        print("Quantity Updated")

    def SearchProductByName(self, name):
        if self.name == name:
            print("Product Found")
        else:
            print("Product Not Found")

    def DisplayProductInformation(self):
        print("Product Name:", self.name)
        print("Product Price:", self.price)
        print("Product Quantity:", self.quantity)



product1 = Product("Laptop", 50000, 10)
product2 = Product("Mouse", 500, 20)
product3 = Product("Keyboard", 1000, 15)
product4 = Product("Monitor", 10000, 8)
product5 = Product("Headphones", 2000, 12)


product1.AddProductDetails()
product1.UpdateProductQuantity(15)
product1.SearchProductByName("Laptop")
product1.DisplayProductInformation()




# Question 7: Security Log Analyzer

# Create a SecurityLog class.

# Tasks
# Store Username and Login Status.
# Count Successful Logins.
# Count Failed Logins.
# Display Total Login Attempts.
# Generate Login Summary.

# Cyber Security Project



class SecurityLog:
    def __init__(self, username, login_status):
        self.username = username
        self.login_status = login_status

    def CountSuccessfulLogins(self):
        if self.login_status == "Success":
            return 1
        else:
            return 0

    def CountFailedLogins(self):
        if self.login_status == "Failed":
            return 1
        else:
            return 0

    def DisplayTotalLoginAttempts(self):
        print("Username:", self.username)
        print("Login Status:", self.login_status)

    def GenerateLoginSummary(self):
        print("----- Login Summary -----")
        print("Username:", self.username)
        print("Login Status:", self.login_status)



log1 = SecurityLog("admin", "Success")
log2 = SecurityLog("user1", "Failed")
log3 = SecurityLog("user2", "Success")
log4 = SecurityLog("user3", "Failed")
log5 = SecurityLog("user4", "Success")


successful_logins = (
    log1.CountSuccessfulLogins() +
    log2.CountSuccessfulLogins() +
    log3.CountSuccessfulLogins() +
    log4.CountSuccessfulLogins() +
    log5.CountSuccessfulLogins()
)


failed_logins = (
    log1.CountFailedLogins() +
    log2.CountFailedLogins() +
    log3.CountFailedLogins() +
    log4.CountFailedLogins() +
    log5.CountFailedLogins()
)


print("Total Login Attempts:", 5)
print("Successful Logins:", successful_logins)
print("Failed Logins:", failed_logins)


log1.GenerateLoginSummary()



# Question 8: Student Marks Analyzer

# Create a StudentMarks class.

# Tasks
# Accept marks of five subjects.
# Calculate Total Marks.
# Calculate Percentage.
# Calculate Average Marks.
# Display Result.

# Data Analytics Project


class StudentMarks:
    def __init__(self):
        self.marks = []

    def accept_marks(self, subject1, subject2, subject3, subject4, subject5):
        self.marks = [subject1, subject2, subject3, subject4, subject5]

    def calculate_total_marks(self):
        return sum(self.marks)

    def calculate_percentage(self):
        total_marks = self.calculate_total_marks()
        return (total_marks / 500) * 100

    def calculate_average_marks(self):
        total_marks = self.calculate_total_marks()
        return total_marks / 5

    def display_result(self):
        print("----- Student Marks Result -----")
        print("Total Marks:", self.calculate_total_marks())
        print("Percentage:", self.calculate_percentage())
        print("Average Marks:", self.calculate_average_marks())


        if self.login_status == "Success":
            return 1
        else:
            return 0

    def CountFailedLogins(self):
        if self.login_status == "Failed":
            return 1
        else:
            return 0

    def DisplayTotalLoginAttempts(self):
        print("Username:", self.username)
        print("Login Status:", self.login_status)

    def GenerateLoginSummary(self):
        print("----- Login Summary -----")
        print("Username:", self.username)
        print("Login Status:", self.login_status)



log1 = SecurityLog("admin", "Success")
log2 = SecurityLog("user1", "Failed")
log3 = SecurityLog("user2", "Success")
log4 = SecurityLog("user3", "Failed")
log5 = SecurityLog("user4", "Success")

successful_logins = (
    log1.CountSuccessfulLogins() +
    log2.CountSuccessfulLogins() +
    log3.CountSuccessfulLogins() +
    log4.CountSuccessfulLogins() +
    log5.CountSuccessfulLogins()
)


failed_logins = (
    log1.CountFailedLogins() +
    log2.CountFailedLogins() +
    log3.CountFailedLogins() +
    log4.CountFailedLogins() +
    log5.CountFailedLogins()
)


print("Total Login Attempts:", 5)
print("Successful Logins:", successful_logins)
print("Failed Logins:", failed_logins)


log1.GenerateLoginSummary()



# Question 9: Arithmetic Calculator using Functions

# Do not use a class.

# Tasks
# Create an Addition function.
# Create a Subtraction function.
# Create a Multiplication function.
# Create a Division function.
# Create a Menu-Driven Calculator.

# Concepts: User Defined Functions



def Addition(a, b):
    return a + b


def Subtraction(a, b):
    return a - b


def Multiplication(a, b):
    return a * b


def Division(a, b):
    return a / b


print("----- Calculator -----")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

option = int(input("Enter your option: "))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if option == 1:
    print("Result:", Addition(a, b))

elif option == 2:
    print("Result:", Subtraction(a, b))

elif option == 3:
    print("Result:", Multiplication(a, b))

elif option == 4:
    print("Result:", Division(a, b))

else:
    print("Invalid Option")



# Question 10: Data Analytics Function Library

# Create separate functions.

# Tasks
# Calculate Sum.
# Calculate Average.
# Find Maximum Value.
# Find Minimum Value.
# Find Total Number of Records.

# Concepts: User Defined Functions





def CalculateSum(numbers):
    return sum(numbers)


def CalculateAverage(numbers):
    return sum(numbers) / len(numbers)


def FindMaximum(numbers):
    return max(numbers)


def FindMinimum(numbers):
    return min(numbers)


def FindTotalRecords(numbers):
    return len(numbers)



numbers = [10, 20, 30, 40, 50]

print("Data:", numbers)

print("Sum:", CalculateSum(numbers))
print("Average:", CalculateAverage(numbers))
print("Maximum:", FindMaximum(numbers))
print("Minimum:", FindMinimum(numbers))
print("Total Number of Records:", FindTotalRecords(numbers))