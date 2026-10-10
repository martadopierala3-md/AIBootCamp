import numpy as np 

# #array and scalar bradcasting
# #Broadcasting in Python usually refers to NumPy automatically expanding arrays of compatible shapes during operations.
# import numpy as np

# a = np.array([1, 2, 3])
# b = 10

# print(a + b)  # [11 12 13]
# #NumPy “broadcasts” 10 across every element of a.

# #Another example: The smaller array is applied across matching dimensions. Shapes are compatible when their dimensions are equal or one of them is 1.
# a = np.array([[1, 2, 3],
#               [4, 5, 6]])
# b = np.array([10, 20, 30])

# print(a + b)
# # [[11 22 33]
# #  [14 25 36]]

# matrix =np.array([[1,2,3],[4,5,6]])
# print("Original matrix: \n", matrix)
# vector = np.array([1,0,1])
# print("broadcasted matrix :\n", vector + matrix)

#AGREGATE fUNCTIONS: NumPy provides a variety of aggregate functions that can be applied to arrays, such as sum, mean, min, max, etc. 
# These functions can be applied to the entire array or along specific axes.

#arr = np.array ([[1, 2, 3],[4, 5, 6]])

# print("Sum: ", np.sum(arr)) # Sum of all elements
# print("Mean: ", np.mean(arr)) # Mean of all elements
# print("Max: ", np.max(arr)) # Maximum element
# print("Min: ", np.min(arr)) # Minimum element
# print("Standard deviation: ", np.std(arr)) # Standard deviationof all elements
# print("Sum along axis rows: ", np.sum(arr, axis=1)) # Sum along rows
# print("Sum along axis columns: ", np.sum(arr, axis=0)) # Sum along columns

# #BOOLEAN INDEXING: Boolean indexing allows you to select elements from an array based on a condition.
# arr = np.array([1,2,3,4,5,6])
# evens = arr[arr % 2 == 0] 
# print("Evens: ", evens) #filtering even numbers from the array

# #modyfy arr based on conditions changing all elements greater than 3 to 0
# arr[arr > 3] = 0
# print ("modified arr: ", arr)

#random number generation: NumPy provides functions to generate random numbers, which can be useful for simulations, testing, and more.
# setting a seed for reproducibility np.random - module seed(0) 
np.random.seed(42) # setting a seed for reproducibility
random_array = np.random.rand(3,3) # generates a 3x3 array of random numbers between 0 and 1
print("Random numbers: \n", random_array)

# creating integers 
random_integers = np.random.randint(0, 10, size=(2,3)) # generates a 2x3 array of random integers between 0 and 10)
print("Random integers: \n", random_integers)

arr = np.array ([[1, 2, 3],[4, 5, 6]])
arr[arr > 3] = 0
print("Modified arr: ", arr)
#setting a seed for reproducibility
#np.random.seed(0)
#Important note: A seed does not make random numbers “more random.”
#It just makes the output predictable and repeatable.
#If you want, I can also explain how random seed works in Python specifically or how it differs from “true randomness.”