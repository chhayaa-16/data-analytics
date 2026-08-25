#   10-8-26 =====assignment que=========



# 20 MID-LEVEL PRACTICAL QUESTIONS
# NumPy + Matplotlib Numeric and Chart Operations

# COMMON RULES FOR ALL 20 QUESTIONS
# - Take data using user input.
# - Use NumPy arrays for numerical processing.
# - Use Matplotlib for visualization.
# - Use functions to organize the program.
# - Use a class where appropriate.
# - You may use a user-defined module for calculations/visualization.
# - Do not use exception handling.
# - Do not use Scatter Plot or Box Plot.

# 1. STUDENT MARKS ANALYSIS
# Take marks of students in 5 subjects.

# Tasks:
# 1. Create a NumPy array containing marks of all students.
# 2. Calculate each student's total and average marks.
# 3. Find the student with the lowest average marks.
# 4. Sort students according to total marks.
# 5. Find unique grades from the calculated results.
# 6. Create Bar Chart + Histogram of student performance.

# Hints:
# np.array(), np.sum(), np.mean(), np.argmin(), np.sort(), np.unique(), plt.bar(), plt.hist()



# import numpy as np

# def calculate_total(marks):

#     total = np.sum(marks, axis=1)

#     return total



# def calculate_average(marks):

#     average = np.mean(marks, axis=1)

#     return average


# def find_lowest_average(names, average):

#     index = np.argmin(average)

#     lowest_name = names[index]
#     lowest_average = average[index]

#     return lowest_name, lowest_average

# def calculate_grades(average):

#     grades = []

#     for avg in average:

#         if avg >= 90:
#             grades.append("A+")

#         elif avg >= 80:
#             grades.append("A")

#         elif avg >= 70:
#             grades.append("B")

#         elif avg >= 60:
#             grades.append("C")

#         elif avg >= 50:
#             grades.append("D")

#         else:
#             grades.append("F")

#     return np.array(grades)


# def sort_students(names, total):

#     index = np.argsort(total)[::-1]

#     sorted_names = np.array(names)[index]
#     sorted_total = total[index]

#     return sorted_names, sorted_total



# def find_unique_grades(grades):

#     unique_grades = np.unique(grades)

#     return unique_grades







#  que 2 

# 2. MONTHLY SALES ANALYSIS
# Take sales data of 5 products for 12 months.

# Tasks:
# 1. Create a 2D NumPy array for monthly sales.
# 2. Calculate total annual sales of every product.
# 3. Find the product having the minimum annual sales.
# 4. Reshape the sales data into the required structure for analysis.
# 5. Find unique sales values.
# 6. Display Line Chart + Bar Chart of product sales.

# Hints:
# np.array(), np.sum(), np.argmin(), np.reshape(), np.unique(), plt.plot(), plt.bar()


import numpy as np



def s_array(sales_data):
    sales_array = np.array(sales_data)
    return sales_array


def anual_sale(sales_array):
    annual_sales = np.sum(sales_array, axis=0)
    return annual_sales
    # return np.sum(sales_array,axis=1)
      

def min_product(annual_sales):
    min_index = np.argmin(annual_sales)
    return min_index


def reshape_sales(sales_array):
    reshaped_data = np.reshape(sales_array, (12, 5))
    return reshaped_data



def uni_sales(sales_array):
    unique_values = np.unique(sales_array)
    return unique_values



def month_sales(sales_array):
    monthly_sales = np.sum(sales_array, axis=1)
    return monthly_sales