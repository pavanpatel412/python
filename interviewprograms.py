# how to convert list into tuple...
students = ["pavan","raju","kiran","somesh","nani"]
convert_tuple = tuple(students)
print("required tuple is :",convert_tuple)
# what ways can you make an empty NumPy array?
import numpy as np
# method one
empty_array = np.array([])
print(empty_array)
# method 2
empty_array1 = np.empty(shape=(3,3))
print(empty_array)
# How do you print the summation of all the numbers from 1 to 101?
summation = sum(range(1,102))
print(summation)
# n a function, how do you create a global variable?
# global variable is applicabele to any function by ur requirements....
# for exmple..
name = "pavan"
def modify_name():
    name = "raju"
    print(name)
def original_name():
    print(name)
modify_name()
original_name()
# using yeild...
def creating_gen(index):  
    months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']  
    yield months[index]  
    yield months[index+2]  
next_month = creating_gen(7)  
print(next(next_month), next(next_month))  
