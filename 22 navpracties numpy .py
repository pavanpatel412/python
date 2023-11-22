import numpy as np
arrray = np.array([3,4,6,7,8,9,9,0])
print("reshaping array is:\n",arrray.reshape(2,2,2))
print("index of arrray is:\n",arrray[5])
arrray[5] = 89
print("replacing the element 5 to 89 is:\n",arrray)
print("slicing between 3 to 9 is:\n",arrray[0:5])#end index does not printed:
print("reversing the elements in the 1d array:\n",arrray[::-1])
array2 = np.array([[[[2,3,7,4,2,7],[3,5,6,7,8,9],[2,3,4,5,5,6]],[[8,5,6,7,3,5],[2,1,3,7,5,4],[9,5,4,2,6,9]]]])
print("the number of elements in the array:\n",array2.size)
print("shape of  the array:\n",array2.shape)
print("the number of dimensions in the array:\n",array2.ndim)
print("the datatype of the array:\n",array2.dtype)
print("reshape the arra2 to 2,1,6,3 is:\n",array2.reshape(2,1,6,3))
print("reshape the arra2 to 6,6is:\n",array2.reshape(6,6))
print("reshape the arra2 to 1,4,9 is:\n",array2.reshape(1,4,9))
array3 = np.array([[2,3,7,4,2,7],[3,5,6,7,8,9],[2,3,4,5,5,6],[8,5,6,7,3,5],[2,1,3,7,5,4],[9,5,4,6,5,6]])#it can't work in 3 , more dimensions it can works only in 2d and 1d:

print("reversing the array rows in the array2 is:\n",array3[::-1])
print("find the  4 element in the last row is :\n",array3[5,2])
print(" in array3 how many of them are >7 is:\n",array3>=7)
np.save("c:\\newfile\\SOMESH2",array3)#to save the array in some file
loadarray =np.load("c:\\newfile\\SOMESH2.npy")
print("the loaded array is:\n",loadarray)

