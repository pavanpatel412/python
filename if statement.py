# A company decided to give bonus of 5% to employee if his\her year of service is more than 5yrs ask user or their salary and year of service and print the net bonous amount>
# salary = input("enter the salary:")
# # print("salary is:",salary)
# yos = input("enter your year of service:")
# if ('yos')>('5'):
#     salary2 = 5*(salary)
#     print("bonus is:\n",salary2)
# else:
#     print("no bonus:")
# # take  values of length and breadth of a rectangle from user and check if it is square or not:
# length = input("enter the length:")
# breadth = input("enter the breadth:")
# if (length==breadth):
#     print("it is rectangle traingle:")
# else:
#     print("it is ot a rectangle traingle")
# # take two int values from user and print greatest among them:
# user = int(input("enter some integer"))
# user2 =int(input("enter some integer"))
# if (user>user2):
#     print("the greatest number is",user)
# elif(user2>user):
#     print("the greatest number is:",user2)
# else:
#     print("both are equal....")
# A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit until will cost 100.
# Judge and print total cost for user>
# quantity = input("enter the quantity:\n")
# if (quantity*100>'1000'):
#     print("cost is\n",((quantity*100)-(.1*quantity*100)))
# else:
#     print("cost is:\n",quantity*100)

# # take input of age of 3 people by user and determine oldest and youngest among them:
first = input("enter the first person age:")
second = input("enter the seecond person age:")
third = input("enter the third person age:")
if (first>=second)&(first>=third):
    print("first person is oldest person")
elif(second>=first)&(second>=third):
    print("second person is oldest person")
if (third>=second)&(first<=third):
    print("third person is oldest person")
else:
    print("all are same")