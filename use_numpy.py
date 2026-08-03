# NUMPY + FUNCTIONS + USER-DEFINED MODULE + BAR/PIE CHART TOP 18 PRACTICAL
# QUESTIONS

# Requirements: - Use NumPy - Use user-defined functions - Use
# user-defined modules - Use Bar Charts - Use Pie Charts - No Pandas - No
# ready-made analysis functions beyond what is required - Each question
# contains 6 practical tasks

# 1.  STUDENT MARKS ANALYSIS

# Create a NumPy array containing marks of 10 students in 5 subjects.

# Tasks: 1. Create a function to calculate total marks of every student.
# 2. Create a function to calculate the average marks of every student. 3.
# Create a function to find the student with the highest total marks. 4.
# Create a bar chart showing each student’s total marks. 5. Create a pie
# chart showing the percentage contribution of each student’s total marks.
# 6. Move the calculation functions into a user-defined module and import
# them into the main program.



import numpyyy as np

mark=np.array([
    [65,788,56,33,98]
    [34,98,23,77,56,]
    [77,35,96,75,84]
])

def total():
    return np.sum(mark, axis=1)

def average ():
    return np.mean(mark,axis=1)


def highest_mark ():
    totals =np.sum(mark, axis =1)
    return np.argmax(totals)

def per ():
    totals = np.sum(mark, axis=1)
    percentage = np.sum(totals)
    return (totals*100)/percentage
     



