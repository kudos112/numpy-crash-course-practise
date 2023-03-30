# import numpy as np

# Slicing

# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# consider it as a matrix
# on printing this array it will look like matrix as below
# [[1 2 3 4]
#  [5 6 7 8]]
# print(a)

# Indexing
# print(a[0, 0])  # same a[0][0] => 1
# print(a[1, 2])  # same a[1][2] => 7

# Slicing
# print(a[0, :])  # => [1 2 3 4]
# print(a[0, 2:])  # => [3 4]
# print(a[0, 2:3])  # => [3]
# print(a[0, 0:3])  # => [1 2 3]

# print(a[:, 0])  # => [1 5]
# print(a[1:, 0])  # => [5]
# print(a[0:1, 0])  # => [1]
# print(a[0:2, 0])  # => [1 5]
# print(a[0:3, 0])  # => [1 5] also same because it has length of 2 only

# Negative Indexes
# print(a[-1, -2])  # => 7
# print(a[-1, -1])  # => 8

# # Boolean Indexing
# a = np.array([[1, 2], [3, 4], [5, 6]])
# bool_idx = a > 2  # greater than 2 will be replaced by True and rest by False
# # output will be
# # [[False False]
# #  [ True  True]
# #  [ True  True]]
# print(bool_idx)
# # will return 1-dim array of all greater than 2 items => [3 4 5 6]
# print(a[bool_idx])
# # one liner
# print(a[a > 2])
# # another example
# print(a[a % 2 == 0]) # => [2 4 6]

# using np.where(condition, valuesFromArray in case of true, value in case of false)
# print(np.where(a>2, a, -1))
# # output
# [[-1 -1]
#  [ 3  4]
#  [ 5  6]]

# # Fancy Indexing
# a = np.array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
# b = np.array([0, 1, 2])
# c = np.array([3, 4, 5])
# print(a[b])  # => [10 11 12]
# print(a[c])  # => [13 14 15]

# # get even numbers using Fancy Indexing
# a = np.array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
# even = np.argwhere(a % 2 == 0).flatten()
# print(even)  # => [ 0  2  4  6  8]
# print(a[even])  # => [10 12 14 16 18]
