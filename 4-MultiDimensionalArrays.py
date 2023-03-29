import numpy as np

# # 1-Dimensional Array
# a = np.array([1, 2, 3])
# print(a)
# print(a.ndim)

# # 2-Dimensional Array
# b = np.array([[1, 2, 3], [4, 5, 6]])
# print(b)
# print(b.ndim)

# # 3-Dimensional Array
# c = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
# print(c)
# print(c.ndim)

# example array for next operations
a = np.array([[1, 2, 3], [4, 5, 6]])

# # extract values from multi-dimensional array
# print(a[0][0]) # => 1
# print(a[0,0]) # => 1

# # Slicing
# # all the rows values from 0 column
# print(a[:, 0])  # => [1 4]
# # all the column values from 0 row
# print(a[0, :])  # => [1 2 3]

# # Transpose of the array
# print(a.T) # => [[1 4] [2 5] [3 6]]

# Inverse of array or matrix
# print(np.linalg.inv(a)) # => returns error because only square matrix can have inverse So
# b = [[1, 2], [3, 4]]
# print(np.linalg.inv(b)) # => [[-2.   1. ] [ 1.5 -0.5]]

# Determinant of array or matrix
# print(np.linalg.det(a)) # => returns error because only square matrix can have determinant So
# b = [[1, 2], [3, 4]]
# print(np.linalg.det(b)) # => -2.0000000000000004

# Diagonal of array or matrix
# print(np.diag(a)) # => [1 5]

# Diagonal Matrix of array or matrix
# diag = np.diag(a)
# print(np.diag(diag)) # => [[1 0] [0 5]]

