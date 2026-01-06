'''
we use 
np.nan_to_num(array, nan = value ) Default value is 0
'''

import numpy as np

arr = np.array([1,2,np.nan, 4,np.nan, 6])

replace_value = np.nan_to_num(arr)
another_value = np.nan_to_num(arr, nan = 100)

print(replace_value)

print(another_value)
