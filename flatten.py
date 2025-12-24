'''
.ravel() -> it returns a view 
.flatten() -> it returns a copy 
Both methods return a 1D array.
The difference is that ravel() returns a flattened view of the original array, while flatten() returns a new array that is a copy of the original array flattened to 1D.
If the original array is modified, ravel() will reflect those changes, while flatten() will not.
'''

import numpy as np

arr = np.array([[1,2,3], [4,5,6]])

print(arr.ravel())

print(arr.flatten())
