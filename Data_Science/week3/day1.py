import numpy as np

A = np.array([[1,2], [3,4]])
B = np.array([[5,6], [7,8]])


print("Addition \n" , A+B)
print("Substraction \n", A-B)

C=2*A 
print("Scalar Mutiplication \n" , 2*A)
#matrix mutiplication numeber of rows and columns needs to match between two matrix 

result = np.dot(A,B)
print("Matrix Mutiplication \n" , result)

#Identity Matrix: is a special square matrix containing: 1 on the main diagonal, 0 everywhere else.
IdentityM = np.eye(5)
print("Identity matrix\n" , IdentityM)

ZeroM = np.zeros((5,3))
print("Zero matrix\n" , ZeroM)

# A diagonal matrix is a square matrix in which all elements outside the main diagonal are zero.

DiagM = np.diag((5,3,2,1))
print("Diagonal matrix\n" , DiagM)