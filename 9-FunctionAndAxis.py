# import numpy as np    

# # Functions with parameter axis
# # axis have values like None, 0, 1, could be more i don't know

# # all the below functions are also accessable via NumPy object
# # like np.functionName(arrayName, axis=optional)

# # sum function (by default it has parameter axis=None )
# a = np.array([2, 2, 2])
# print(a.sum()) # => 9
# print(a.sum(axis=None)) # => 9

# # # changing axis to 0
# a = np.array([2, 2, 2])
# print(a.sum(axis=0))  # => 9

# # # changing axis to 0 (add values across columns vertically)
# a = np.array([[2, 2, 2], [2, 2, 2]])
# print(a.sum(axis=0))  # => [4 4 4]

# # # changing axis to 1 (add values across rows horizontally)
# a = np.array([[2, 2, 2], [2, 2, 2]])
# print(a.sum(axis=1))  # => [6 6]

# # Finding mean using np.mean(axis) or arrayName.mean(axis)

# # # # with axis = None
# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(a.mean(axis=None))  # => 4.5

# # # # changing axis to 0 (vertically)
# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(a.mean(axis=0))  # => [3.0 4.0 5.0 6.0]

# # # # changing axis to 1 (horizontally)
# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(a.mean(axis=1))  # => [2.5 6.5]

# # # Find Standard Deviation
# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(a.std(axis=None))  # => 2.29128784747792

# # # changing axis to 0 (vertically)
# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(a.std(axis=0))  # => [2. 2. 2. 2.]

# # # changing axis to 1 (horizontally)
# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(a.std(axis=1))  # => [1.11803399 1.11803399]


# # # Find Variance
# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(a.var(axis=None))  # => 5.25

# # # changing axis to 0 (vertically)
# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(a.var(axis=0))  # => [4. 4. 4. 4.]

# # # changing axis to 1 (horizontally)
# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(a.var(axis=1))  # => [1.25 1.25]
