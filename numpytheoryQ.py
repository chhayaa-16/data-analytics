# # NumPy Assignment (20 Questions)
# # Section A: Basics (1–5)
# # 1. What is NumPy? Why is it preferred over Python lists for numerical computations?

# # answer---
# #  Numpy stand for numerical python , use for numerical calculations also create array.
#     # it is easy to calculation on arrays single element




# # 2. Explain the difference between a Python list and a NumPy array.

# # answer---- list has store multiple datatype 
# #            - it has a multiple lines of code to fetch the element .
# #            - In list we cant add multidimentional values 


# #             Array- arrays contain same datatype.
# #             -  easy for numerical calculations in each element.
# #             - we can create a one or two diementional array


# # 3. Write the steps to install NumPy and import it in Python.

# # answer-- 1- pip install numpy (write in terminal)
# #          2- then create a file and for import it write a first line of code is import numpy as np





# # 4. What is an ndarray in NumPy?

# # answer---ndarray stand for  N-dimensional array.
# #         usnig this we can create multidimentional arrays. 


# # 5. Explain the importance of NumPy in data science and machine learning.

# # answer--- in data science , we had a number of calculative concepts , and numpy library provide function like
# #             numpy does-  array creation, Mean, Sum, Minimum, Maximum ,Standard deviation



# Section B: Creating Arrays (6–8)
# 6. Write Python code to create a 1D and a 2D array using NumPy.


# 1D array--
# array = np.array([1, 2, 3, 4])

# print(array)

# 2D array--
# arr = np.array([
#     [1, 2],
#     [3, 4]
# ])

# print(arr)


# 7. What is the difference between np.array(), np.zeros(), and np.ones()?

# answer-- np.array()---- create array when we provide a values .

#         np.zeros()---- creates an array with all values are 0 ,we just add a count number.

#          np.ones()---- creates an array with all values are 1 ,we just add a count number.




# 8. Create an array of numbers from 1 to 20 using NumPy.

# answer---

# arr = np.arange(1, 21)

# print(arr)


# Section C: Indexing & Slicing (9–11)
# 9. Explain array indexing in NumPy with an example.

# ans--- used to access any value from array and it start with 0 . 
        

#         arr = np.array([1, 2, 3, 4, 5])

#         here, 1 has 0 Index
#               2- 1
#               3- 2
#               4-3
#               5-4


# 10. What is array slicing? Write a program to extract elements from index 2 to 6.



# 11. How is indexing different in 1D and 2D arrays?




# arr = np.array([1, 2,3, 4])

# print(arr[2])

# for two D array----

# arr = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])
# print(arr[1, 1])




# Section D: Data Types & Copy/View (12–14)
# 12. What are NumPy data types (dtype)? Name any five.

# answer--- it shows which type of data type we have in our data 
#             types--- int , float, bool ,string



# 13. Explain the difference between copy and view in NumPy.
# 14. Write a program to show how modifying a view affects the original array.

# Section E: Shape, Reshape & Iteration (15–16)
                                      
# 15. What is the difference between shape and reshape()?


# ans---- shape -- shows the diamenion of array , it is 1d or 2D , 
#         it returns how many rows and columns we have


#         reshape---it creates a multidiamensional array (matrix veiw) from simple array data.
        




# 16. Write a program to iterate through a 1D and a 2D array.


# import numpy as np

# arr = np.array([10, 20, 30, 40])

# for value in arr:
#     print(value)




#  for 2D array---


#  arr2 = np.array([
#     [10, 20],
#     [30, 40]
# ])

# for row in arr2:
#     print(row)


    



# Section F: Join, Split, Search & Sort (17–20)
# 17. Explain how to join arrays in NumPy using concatenate() or stack().

# import numpy as np

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])

# result = np.concatenate((arr1, arr2))

# print(result)



# stack----

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])

# result = np.stack((arr1, arr2))

# print(result)




# 18. Write a program to split an array into 3 parts.

# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12])

# result = np.array_split(arr, 3)

# print(result)



# 19. What is array searching in NumPy? Explain where() with an example.
# 20. Write a program to sort an array in ascending and descending order.

# assending------------
# import numpy as np

# arr = np.array([5, 1, 4, 2, 3])

# ascending = np.sort(arr)


# print(ascending)



# descending------


# import numpy as np

# arr = np.array([5, 1, 4, 2, 3])


# descending = np.sort(arr)[::-1]


# print("Descending order:")
# print(descending)
