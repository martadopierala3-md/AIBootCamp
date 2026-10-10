#Perform singular value decomposition (SVD) on matrix A.

import numpy as np

A= np.array([[3, 1, 1], [-1, 3, 1], [1, 1, 3]])

U, S, Vt = np.linalg.svd(A)

print("A matrix (Macierz A:\n", A)
print("U matrix (Macierz U):\n", U)
print("S matrix (Macierz S):\n", S)     
print("V transpose matrix (Macierz V^T):\n", Vt)

#Reconstructing the original matrix A from U, S, and Vt:
Sigma = np.zeros((3,3))
np.fill_diagonal(Sigma, S)
reconstructed_A = U @ Sigma@ Vt
print("Reconstructed A matrix (Odtworzona macierz A):\n", reconstructed_A)



