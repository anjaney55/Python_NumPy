'''
Built-in functions in NumPy are designed to handle missing values efficiently.
They can ignore NaN values in calculations, ensuring that the results are accurate without manual intervention.

'''
# np.isnan(array) is used to check for NaN values in an array.
# np.nan_to_num() is used to replace NaN values with a specified number, typically zero.
# np.isinf() is used to check for infinite values in an array.

import numpy as np

arr = np.array([1,2,np.nan, 4,np.nan, 6])

print(np.isnan(arr))


'''
Interview
No,
We cannot compare it directly 
print(np.nan == np.nan)'''