# import numpy as np

# Reshaping

# a = np.array([1, 2, 3, 4])
# print(a)  # => [1 2 3 4]
# # retruns shape in (rows, columns)
# print(a.shape)  # => (4,)

# # reshapes the current array with no change in size and its values
# b = a.reshape(2, 2)
# # [[1 2]
# #  [3 4]]
# print(b)

# # b = a.reshape(2,3) # => returns error because this size requires 6 elements in array to reshape
# # b = a.reshape(1,1) # => returns error because this size requires 2 elements in array to reshape

# Another way to transform the array

# a = np.arange(1,7) # => creates array from 1 to 6
# print(a) # => [1 2 3 4 5 6]

# b = a[np.newaxis, :]
# print(b) # => [ [1 2 3 4 5 6] ]
# print(b.shape) # => (1, 6)
# print(b.ndim) # => 2

# # some excersize with newaxis
# print(a[np.newaxis, :4]) # => [[1 2 3 4]]
# print(a[np.newaxis, 2:4]) # => [[3 4]]
# print(a[np.newaxis, 2:]) # => [[3 4 5 6]]
# print(a[np.newaxis, 3]) # => [4]

# b = a[:, np.newaxis]
# print(b) 
# output
# [[1]
#  [2]
#  [3]
#  [4]
#  [5]
#  [6]]
# print(b.shape) # => (6, 1)
# print(b.ndim) # => 2
