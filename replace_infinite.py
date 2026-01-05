
# np.nan_to_num(array, posinf = value, neginf = value)

# 'posinf' means positive infinite

# 'neginf' means nedative infinite

import numpy as np

arr = np.array([1,2,np.inf, 4,-np.inf, 6])  #np.inf means infinite values in array

cleaned_data = np.nan_to_num(arr, posinf = 1000 , neginf = -1000)

print(cleaned_data)
