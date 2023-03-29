# import numpy as np

# # Dot product in different ways
# # Tip at the end

# # python lists
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]

# # Numpy arrays
# a1 = np.array([1, 2, 3])
# a2 = np.array([4, 5, 6])

# # dot product with python list
# dot = 0
# for i in range(len(l1)):
#     dot += l1[i] * l2[i]
# print(dot)

# # dot product with numpy array
# dot = np.dot(a1, a2)
# print(dot)

# # using another way
# sum = a1 * a2
# dot = np.sum(sum)
# # one liners
# # dot = np.sum(a1 * a2) 
# # dot = (a1 * a2).sum() 
# print(dot)

# # new and concised but remember, it will be used 
# dot = a1 @ a2
# print(dot)

# # # Tip Time
# NumPy Dot Product's execution is much quick and efficient than the manual way
