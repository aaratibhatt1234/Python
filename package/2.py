import numpy as np

A = np.array([[2, 9], [1, -1], [8, 2]])  # Coefficients
b = np.array([3, 1, 4])  # Constants

x_ls = np.linalg.lstsq(A, b, rcond=None)[0]  # Least squares solution
print("Least Squares Solution:", x_ls)