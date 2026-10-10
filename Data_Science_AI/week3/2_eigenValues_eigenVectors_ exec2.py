#Calculate eigenvalues, and eigenvectors.

import numpy as np   

A = np.array([[4, -2], [1, 1]])

eigenValues, eigenVectors = np.linalg.eig(A)

print("EigenValues A (Wartości własne: A) \n", eigenValues)
print("EigenVectors A \n Wektory własne (kolumny):\n", eigenVectors)

