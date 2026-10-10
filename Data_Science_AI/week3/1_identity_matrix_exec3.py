import numpy as np

A= np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
IndentityM = np.eye(3)
print("Identity Matrix \n", IndentityM)
print("A * Identity Matrix \n", np.dot(A,IndentityM))


DiagonalM = np.diag((1, 7, 9))
print("Diagnonal Matrix\n", DiagonalM)

ZeroM = np.zeros((3,3))
print("Zero Matrix \n", ZeroM)