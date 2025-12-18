# The shape of an array is a tuple representing the size of each dimension.
# The size of an array is the total number of elements in the array.
# The ndim attribute gives the number of dimensions of the array.


import numpy as np

arr = np.array([[34,56,32], [34,89,23]])

print(arr.shape)
print(arr.size)
print(arr.ndim)  # Number of dimensions
print(arr.dtype)  # Data type of the elements in the array

