## This script creates a NumPy array with a sequence of numbers 
# using the arange function.
# The arange function generates values within a specified range with a defined step size.
#syntax: np.arange(start, stop, step)

import numpy as np

arr = np.arange(1,10,2) # Create an array with a sequence of numbers from 1 to 9 with a step of 2
print(arr)  # Output: [1 3 5 7 9]