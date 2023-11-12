# numpy NumPy is a Python library used for working with arrays. It also has functions for working in domain of linear algebra..........
import numpy as np
arr = np.array([2,3,4,7,7])
print(arr)
print("the length of the array is :",arr.size)
print("the shape  of the array is :", arr.shape)
print("the datatype of the array is :", arr.dtype)
print("the dimension of the arrays is:", arr.ndim)
# ============================================//
arr2 = np.array([[[[2,3,4,7,7],[2,5,6,7,9],[2,3,4,7,7],[2,5,6,7,9]]]])
print(arr2)
print("the length of the array is:",arr2.size)
print("the shape  of the array is :", arr2.shape)
print("the datatype of the array is :", arr2.dtype)
print("the dimension of the arrays is:", arr2.ndim)
arr3 = np.array([[[[[[8,9],[5,7],[8,9]]]]]])
print(arr3.shape)
# =====================================
# creating an array with zeros..
zeroes_array = np.zeros((2,3))
print("\n zeroes array is:")
print(zeroes_array)
# creating an array with ones.........
ones_array = np.ones((4,5))
print("\ones array is:")
print(ones_array)
print("the size of the array is:",ones_array.size)
print("the shape of the array is:",ones_array.shape)
print("the dimension of the array is:",ones_array.ndim)
