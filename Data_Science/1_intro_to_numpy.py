# NumPy is important for AI because it gives the foundation for handling the numerical data that AI models use every day.
# Why it matters:
# AI models work with large arrays and matrices of numbers.
# NumPy makes those operations fast and efficient.
# It supports vectorized computation, so you can do math on whole arrays instead of looping element by element.
# This is critical for training models, transforming data, and processing tensors and embeddings.
# Key reasons:
# Speed: NumPy is implemented in optimized C code, so it is much faster than pure Python loops.
# Simplicity: It gives a clean way to work with multi-dimensional arrays.
# Data preparation: AI pipelines often involve normalization, feature scaling, matrix multiplication, and statistical calculations.
# Foundation for ML libraries: frameworks like PyTorch and TensorFlow are built around array-based math, and NumPy is the standard language for that style of computation.
# Easy math operations: dot products, matrix multiplication, reshaping, filtering, and aggregations are straightforward.

import numpy as np
# #CREATING ARRAYS
# #create array form a list
# arr = np.array([1, 2, 3, 4])
# #print(arr)
# #using numpy to perform operations on the array

# # zero array
# zeros =np.zeros((3,3))
# #print("Zero Array:\n", zeros)

# # one array
# ones = np.ones((2,4))
# #print("One Array:\n", ones)

# # arange 
# range_array = np.arange(1, 100, 2)
# #print("Range Array:\n", range_array) # creates a NumPy array with numbers starting at 1, stopping before 10, and moving in steps of 2.

# #linspace
# linspace_array = np.linspace(0, 100, 10) # like dividing an interval into equal parts
# # creates evenly spaced values, includes both start and stop, best when you want a fixed number of values
# #print("Linspace Array:\n", linspace_array)

# #Manipulating Arrays
# #reshaping  
# arr = np.array([[1, 2, 3, 4, 5, 6]])
# reshaped = arr.reshape(3, 2) # reshapes the array into 3 rows and 2 columns
# #print("Reshaped Array:\n", reshaped)

# # add dimention
# arr = np.array([1, 2, 3])
# expanded = arr[:, np.newaxis] #is a new dimension at the specified axis (0 means adding a new row)
# #print("Expanded Array:\n", expanded)

# #ELEMENTWISE OPERATIONS
# a = np.array([1,2,3])
# b = np.array([4,5,6])
# print(a + b)  # element-wise addition
# print(a * b)  # element-wise multiplication
# print(a / b)  # element-wise division

# arr = np.array([4,9,16,25])
# print(np.sqrt(arr))  # square root of each element
# print(np.sum(arr))  # sum of all elements
# print(np.mean(arr))  # mean of all elements
# print(np.max(arr))  # maximum value in the array

# ARRAYS INDEXING, SLICING AND RESHAPING
#indexing geting particulkar element from the array
arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[0])  # get the first element
print(arr[-1])  # get the last element  


#slicing geting a range of elements from the array
print(arr[1:4])  # get elements from index 1 to 3 excluding last element
print(arr[:3])  # get elements from start to index 2
print(arr[3:])  # get elements from index 3 to the end

#reshaping changing the shape of the array
reshaped = arr.reshape(2, 3)  # reshape to 2 rows and 3 columns
print("Reshaped Array:\n", reshaped)

