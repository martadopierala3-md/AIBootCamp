#Calculate the determinant of matrix A and its inverse, 
import numpy as np

A = np.array([[2,3,4],[4,5,6],[7,8,10]])

determinant = np.linalg.det(A)
print("Martix A:\n", A)
print("DERERMINANT (Wyznacznik macierzy) A:", determinant)  

inverse = np.linalg.inv(A)
print("INVERSE MATRIX \n(Macierz odwrotna do A:)\n", inverse)

