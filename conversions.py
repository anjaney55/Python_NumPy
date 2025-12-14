# This script demonstrates how to convert a NumPy array of floats to integers.
# The astype method is used for type conversion in NumPy arrays.


import numpy as np

arr = np.array([2.4,5.9,3.6,4.1])

int_arr = arr.astype(int)

print(int_arr)
print(int_arr.dtype)