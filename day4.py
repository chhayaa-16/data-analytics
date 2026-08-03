# Question 1: Student Management System

# Create a Student class.

# Tasks
# Accept Student ID, Name, Age and Course.
# Create a method to display student details.
# Create a method to update the course.
# Create three student objects.
# Display all student information.

# Concepts: Class, Object, Constructor, Methods


class student:
    def __init__(self,studentID,name,age,course):
        self.studentID=studentID
        self.name=name
        self.age=age
        self.course=course





    def display(self):
     print("student ID",self.studentID)
     print("Name",self.name)
     print("age",self.age)
     print("course",self.course)


    def update(self):
       



s1=student(1,"seema",20,"cpp")
s1.display()




   
