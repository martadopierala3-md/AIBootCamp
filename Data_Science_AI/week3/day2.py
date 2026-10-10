import numpy as np
# Eigenvalues and Eigenvectors

# • What are Eigenvalues and Eigenvectors?
# • If A · v = λ · v, then
# • v is an eigenvector
# • λ is the eigenvalue
# • Geometric Interpretation
# • Eigenvectors point in the direction where the matrix transformation stretches or compresses vectors
# • Eigenvalues indicate the factor of stretching or compression
# • Properties
# • Matrix of size n × n has n eigenvalues and eigenvectors
# • Eigenvalues can be real or complex
# • For a symmetric matrix, eigenvalues are always real.

# • Czym są wartości własne i wektory własne?
# • Jeżeli A · v = λ · v, wówczas
# • v jest wektorem własnym
# • λ jest wartością własną
# • Interpretacja geometryczna
# • Wektory własne wskazują kierunek, w którym transformacja macierzy rozciąga lub ściska wektory
# • Wartości własne określają czynnik rozciągania lub ściskania
# • Właściwości
# • Macierz rozmiaru n × n ma n wartości własnych i n wektorów własnych
# • Wartości własne mogą być rzeczywiste lub zespolone
# • Dla macie

A = np.array([[2, 3],
              [1, 4]])

determinant = np.linalg.det(A)
print("Martix A:\n", A)
print("DERERMINANT (Wyznacznik macierzy) A:", determinant)

inverse = np.linalg.inv(A)
print("INVERSE MATRIX \n(Macierz odwrotna do A:)\n", inverse)
#print("A pomnożona przez macierz odwrotną:\n", A @ inverse)

eigenValues, eigenVectors = np.linalg.eig(A)
print("EigenValues A (Wartości własne: A) \n", eigenValues)
print("EigenVectors A \n Wektory własne (kolumny):\n", eigenVectors)

B= np.array([[4,2],[1,1]])
eigenValues, eigenVectors = np.linalg.eig(B)
print("EigenValues B (Wartości własne:) \n", eigenValues)
print("EigenVectors B \n Wektory własne (kolumny):\n", eigenVectors)

U, S, Vt =np.linalg.svd(A)

print("U matrix (Macierz U):\n", U)
print("S matrix (Macierz S):\n", S)
print("V^T matrix (Macierz V^T):\n", Vt)

# Introduction to Matrix Decomposition

# • What is Matrix Decomposition?
# • Process of breaking a matrix into simpler components to analyze or solve problems

# • Singular Value Decomposition (SVD)
# • SVD decomposes a matrix A into three matrices: A = U · Σ · V^T
# • U: Left singular vectors (orthogonal matrix)
# • Σ: Diagonal matrix of singular values (non-negative)
# • V^T: Right singular vectors (orthogonal matrix)

# • Applications of SVD

# zym jest dekompozycja macierzy?
# • Proces rozkładania macierzy na prostsze składniki w celu analizy lub rozwiązania problemów
# • Rozkład według wartości osobliwych (SVD)
# • SVD rozkłada macierz A na trzy macierze: A = U · Σ · V^T
# • U: Lewostronne wektory osobliwe (macierz ortogonalna)
# • Σ: Macierz diagonalna wartości osobliwych (nieujemne)
# • V^T: Prawostronne wektory osobliwe (macierz ortogonalna)
# • Zastosowania SVD