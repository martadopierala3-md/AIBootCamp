# broadcasting operations in numpy
import numpy as np
matrix = np.array([[1,2,3],[4,5,6], [7,8,9]])
vector = np.array([1,0,-1])
print("Original matrix: \n", matrix)    

results_add = matrix + vector
print("Result of addition: \n", results_add)

results_mul = matrix * 2
print("Result of multiplication: \n", results_mul)
