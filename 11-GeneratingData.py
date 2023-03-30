# import numpy as np

# # array = matrix

# # zeros matrix
# print(np.zeros((2, 2))) # default data type float64
# print(np.zeros((2, 2), dtype='int64')) # enforce data type as you want

# # Ones Matrix
# print(np.ones((2, 2))) # default data type float64
# print(np.ones((2, 2), dtype='int64')) # enforce data type as you want

# # Custom same value matrix
# print(np.full((2, 2), 7)) # will create matrix of having elements of value 7

# # Identity Matrix
# print(np.eye(3))
# print(np.eye(3, dtype='int64'))

# # 1-d array or row matrix
# print(np.arange(5)) # => [0 1 2 3 4]
# print(np.arange(1, 5)) # => [1 2 3 4]

# # Custom matrix as you want
# # np.linspace(startingValue, endingValue, number of elements)
# print(np.linspace(0, 10, 5)) # => [ 0.   2.5  5.   7.5 10. ]
