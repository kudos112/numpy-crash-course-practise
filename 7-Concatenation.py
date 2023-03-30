# import numpy as np

# # Array Concatenation

# a = np.array([[1, 2, 3, 4],[9, 10, 11, 12]])
# b = np.array([[4, 5, 6, 7]])
# print(a)  # => [1 2 3 4]
# print(b)  # => [5 6 7 8]

# by default np.concatenate has axis = 0
# print(np.concatenate((a, b))) # added b as new row
# [[ 1  2  3  4]
#  [ 9 10 11 12]
#  [ 4  5  7  8]]
# print(np.concatenate((a, b), axis=0))  # same to line 11

# axis = 0 means add as row
# axis = 1 means add as column

# with axis = 1
# returns error because we cannot add row of size 4 as column of size 2 in a
# print(np.concatenate((a, b), axis=1))
# using transpose of b also return error because column of elements 4 cannot be added to column of size 
# print(np.concatenate((a, b.T), axis=1))

# # now try with matrix of having only column with size 2
# c = np.array([[45],[50]])
# print(np.concatenate((a, c), axis=1))
# # output will be
# # [[ 1  2  3  4 45]
# #  [ 9 10 11 12 50]]

# Transpose means turns rows into columns and columns into rows

# # now try with matrix of having only column with size 2
# c = np.array([[45, 50]])
# # print(np.concatenate((a, c), axis=1)) # this will give error because of row into column
# print(np.concatenate((a, c.T), axis=1))
# # output will be same as above after transposing
# # [[ 1  2  3  4 45]
# #  [ 9 10 11 12 50]]

# # Another way using hstack and vstack
# a = np.array([1, 2, 3, 4])
# b = np.array([5, 6, 7, 8])
# # hstack appends array horizontally
# print(np.hstack((a, b))) # => [1 2 3 4 5 6 7 8]
# # vstack appends array vertically
# print(np.vstack((a, b))) 
# # [[1 2 3 4]
# #  [5 6 7 8]]
