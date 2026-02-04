'''
Arrays:
It is collection of homogeneous data elements that can store under a single variable.
Python does not support arrays
NumPy:
 NumPy-->Numerical Python 
It can easily access arrays
Mainly uses in ML,DS,AL Applications
the index value starts with 0 and ends with (n-1), n-->Size of the array 
'''
import numpy as np
arr = np.array([10,20,30])
print(arr)
print(np.max(arr))  # To find the maximum value in the array
print(np.min(arr))  # To find the minimum value in the array
print(np.mean(arr)) # To find the mean value of the array
print(np.sum(arr)) # To find the sum of all elements in the array
