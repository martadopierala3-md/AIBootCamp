#generatre and filter random datasets
import numpy as np

# Generate a random dataset 5:5 matrix between 1 and 50
matrix = np.random.randint(1, 51, size=(5, 5))
print("Original matrix: \n", matrix)

#filter valuse above 25 and replace by 0
matrix[matrix>25]=0
print("Matrix after filtering: \n", matrix)

#cALCULATE SUM, MEAN, MAX, MIN, STD
print("Sum: ", np.sum(matrix)) # Sum of all elements
print("Mean: ", np.mean(matrix)) # Mean of all elements
print("Std: ", np.std(matrix)) # Standard deviation