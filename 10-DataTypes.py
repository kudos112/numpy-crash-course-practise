import numpy as np    

# # Data Types in NumPy
# # if we have int64, this mean integer with size of 64 bits (8 bytes) 

# # # Data types
# a = np.array([1, 2, 3])
# print(a) # => [1 2 3]
# print(a.dtype) # => int64

# # You can enforce data type too
# a = np.array([1, 2, 3], dtype='int32')
# print(a) # => [1 2 3]
# print(a.dtype) # => int32

# # Another Example
# a = np.array([1, 2, 3], dtype='float64')
# print(a) # => [1. 2. 3.]
# print(a.dtype) # => float64

# # You can also transform int to float and float to int
# # In that case they will lose some value
