#Numpy is a zero(0) based index

'''
for slicing syntax is
   arr[start, stop, step]
we have negative idex for reversing arrray'''

import numpy as np

arr = np.array([23,45,2,78,34, 7,89])

print(arr[2:5])

print(arr[:4])  #print 0 to 4

print(arr[3:]) 

print(arr[::2])  # it print every second value

print(arr[::-1])   # it will reverse the array 