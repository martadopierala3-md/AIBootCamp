import numpy as np

M = np.array([[1, 2, 3], [4, 5, 6], [7, 8,9]])
V = np.array([1, 0, -1])

#matrix , vector mutiplication
result = np.dot(M,V)
print("Matrix/ vector  Mutiplication \n" , result)