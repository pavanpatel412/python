# numpy NumPy is a Python library used for working with arrays. It also has functions for working in domain of linear algebra..........
import numpy as np
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
eye_array = np.eye(8,7)
print("\n the eye array is :")
print(eye_array)
#slicing array::is a function in NumPy that is used to create an array of evenly spaced values over a specified range. The syntax for 

linespace = np.linspace(4, 15, num=50, endpoint=False, retstep=True, dtype=int)

print("linespace array is:\n",linespace)
# arange.... it  arange the values with ur given condition
rangearray = np.arange(2,20,2)
print("the arranging the elements is:\n",rangearray)
# it print the random numbers between 0 to 1
random1 = np.random.random()
print("the random number array is:\n",random1)
random = np.random.randint(1,9,8)
print("the randomint array is ;\n",random)
# print("the random array is ;\n",random.size)
# print("the random array is ;",random.shape)
print("the dimension of the arrray")
random_integer = np.random.randint(1,7)  # Generates a random integer between 1 and 9
print("the random integer is nothing but:\n",random_integer)
