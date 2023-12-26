# find given string is palindrom or not:
# def palindrom(string):
#     revrs_string = string[::-1]
#     return string == revrs_string
# string1 = str(input("enter some string:"))
# if palindrom(string1):
#     print("you entering string is palindrom:")
# else:
#     print("you entering string is not a palindrom")
# find a python program to find the factorial of a given number
number = int(input("enter some number:"))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
rsult = factorial(number)
print("factorial of",number,"is",rsult)
# find largest element in the list;
numbers = [34,35,56,66,50,30]
largest_numbr = max(numbers)
print("largest number in the list is",largest_numbr)
# ----------------------------------------------3
students = ["pavan","kiran","durga","ramesh"]
def largest_element(student):
   large =student[0]
   for students in student:
       if students>large:
           large = students
           return large
result = largest_element(students)
print("largest element in the list is:",result)


     
