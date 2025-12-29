'''
How numpy handle arrays of different shapes

1. Matching Dimension : It will be direct and easy
2. Expanding Single element : [1,2,3] + [10] output [11,12,13]
3. Incompatible shapes : [1,2,3] + [2,3] it will through an ERROR

'''

import numpy as np

arr = np.array([10,45,67])

result = arr*2

print(result)