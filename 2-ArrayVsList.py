# import numpy as np

# python list
# l = [1,2,3]
# numpy array
# a = np.array([1,2,3])

# print(l) # => [1, 2, 3]
# print(a) # => [1 2 3]

# add elements in both array
# l.append(4) # => l = [1, 2, 3, 4]
# a.append(4) # it will return an error

# # adding element in different way
# # List will add 4 into array like above
# print(l + [4]) # => l = [1, 2, 3, 4]
# # NumPy array will not add array but add every element of a with 4
# print(a + np.array([4])) #  => [4 5 6] 
# # this method is called broadcasting which is recomended with equal size of array
# # same results with a + np.array([4, 4, 4]) => [4 5 6] which is recomended way

# # multiplication 
# # mutilpying list with 2
# print(l * 2) # => [1, 2, 3, 1, 2, 3]
# # multiplying NumPy array with 2
# print (a * 2) # => [2, 4, 6]
