# create 3x3 array and perform some basic operations

import numpy as np
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original matrix: \n", matrix)

# Transpose the matrix
transpose =   matrix.T
print("Transposed matrix: \n", transpose)

another_matrix =np.array([[9,8,7], [6,5,4], [3,2,1]])
print("Another matrix: \n", another_matrix)
print("matrix addition: \n", matrix + another_matrix)
print("matrix multiplication:\n", matrix * another_matrix)

