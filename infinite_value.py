#np.isinf(array)

import numpy as np

arr = np.array([1,2,np.inf, 4,-np.inf, 6])  #np.inf means infinite values in array

print(np.isinf(arr))

# It return a Boolen value True/False 

# For infinite values in an array