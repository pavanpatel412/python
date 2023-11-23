import numpy as np
array1 = np.array([[1,2,3,4,5],[3,4,5,6,7]])
array2 = np.array([[3,5,6,7,7],[3,5,6,7,8]])
# np.add(): Add corresponding elements of two arrays.
print("adding the two arrays is:\n",np.add(array1,array2))
# np.subtract(): Subtract elements of one array from another.
print("substract the two arrays is:\n",np.subtract(array1,array2))
# np.multiply(): Multiply elements of two arrays.
print("multiplay the two arrays is:\n",np.multiply(array1,array2))
# np.divide(): Divide elements of one array by another.
print("divide the two arrays is:\n",np.divide(array1,array2))
# np.dot(): Dot product of two arrays.
ex1 = np.array(([[3,5],[3,5]]))
ex2 = np.array(([[4,6],[6,8]]))
product = np.dot(ex1,ex2)#it can be applicable for equal rows and colums only
print("dot matrix of the two arrays is:\n",product)
# array.sum(): Sum of array elements.
print("sum of  the array1 is:\n",array1.sum())
# array.mean(): Mean of array elements.
print("mean of the  array2 is:\n",array2.mean())
# array.std(): 
print("std of the  array2 is:\n",array2.std())
