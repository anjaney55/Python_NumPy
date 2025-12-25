'''
reshaping means to change the dimensions without modifing the data
it use in convert 1D to 2D and so on'''

#we use arr.reshape(rows, columns) method for reshaping

#it specifies the new shape if dimensions are match 


import numpy as np

arr = np.array([1,2,3,4,5,6])

print(arr.reshape(3,2))

print(arr.reshape(2,3))

#reshaping does not create copy it returns a view

