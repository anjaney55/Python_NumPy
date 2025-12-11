# This script demonstrates how to create arrays filled with ones, zeros, and a constant value using NumPy.


import numpy as np
one = np.ones(3)   # for ones
zero = np.zeros((3,4)) # for zeros

full_arr = np.full((3,2),6) # for full array with constant value

print(one)
print(zero)
print(full_arr)