# arithametic operators...
# operations in python: using integers
i_integer1 = 23
i_integer2 = 45
result = i_integer1+i_integer2
print("adding i_integer1 and i_integer2 is:",result)
# using float numbers
flt_number1 = 34.67
flt_number2 = 45.6
print("adding flt_number1 and flt_number 2 is:         ",flt_number1+flt_number2)
print(" substraction of flt_number1 and flt_number 2 is:",flt_number1-flt_number2)
print("multiplay of flt_number1 and flt_number 2 is:  " ,flt_number1*flt_number2)
print("division of flt_number1 and flt_number 2 is:    ",flt_number1/flt_number2)
print("modules  of flt_number1 and flt_number 2 is:    ",flt_number1%flt_number2)
print("exeponent of flt_number1 and flt_number 2 is:   ",flt_number1**flt_number2)
print("floor of flt_number1 and flt_number 2 is:       ",flt_number1//flt_number2)
# using complex numbers...in this only 4 conditions can allowed +,-,*,/
cmp_number1 = 20.5j
cmp_number2 = 45.8j
print("adding flt_number1 and flt_number 2 is:         ",cmp_number1+cmp_number2)
print(" substraction of flt_number1 and flt_number 2 is:",cmp_number1-cmp_number2)
print("multiplay of flt_number1 and flt_number 2 is:  " ,cmp_number1*cmp_number2)
print("division of flt_number1 and flt_number 2 is:    ",cmp_number1/cmp_number2)
# print("modules  of flt_number1 and flt_number 2 is:    ",cmp_number1%cmp_number2)
# print("exeponent of flt_number1 and flt_number 2 is:   ",cmp_number1**cmp_number2)
# print("floor of flt_number1 and flt_number 2 is:       ",cmp_number1//cmp_number2)
# in strings 
frst_name = "Pavan"
last_name = "kumar"
concadination = frst_name+last_name
print("the concadination of two strings is:",concadination)
# print(frst_name*last_name)  it can't work in the strings
# print(frst_name*last_name)

# comparision operators like...==,!=,<=,>=,<,>
if frst_name==last_name:
    print("condition is true;")
else:
    print("codition is false;")

if frst_name<=last_name:
    print("satisfy::")
else:
    print("not satisfy")

if frst_name>=last_name:
    print(":first_name is greater than  or equal to last name:")
else:
    print("first name is less than or equla to last name:")
if frst_name!=last_name:
    print(":first_name is not equal to last name:")
else:
    print("first name is equal to last name:")
# membership operators.....
# it may be used in list and tuples and dictionaries 
list1 = [1,2,3,4,5,6,7]
if 2 in list1:
    print("true")
else:
    print("false")
# the output will be in boolean type true or false...
assign = 2  in list1 
print(assign)
print("2 is not in list 1:",2 not in list1)
# int can have 4 byts
# float can have 4 byts
# complex numbers have 4 byts
# boolean can have 2 byts or 0 bites ==> 1 is nothing but true ,0 is nothing but false
# logical operators ==> and,or,not

x =4
y = 5
if x>0 and y>0:
    print("x and y are greater than zero.")
else:
    print("x and y are less than zero:")
age = 18
if age>3 or age>=45:
    print("pavan is elgible for vote")
else:
    print(" he was not eligible for vote:")
its_raining = True
if not its_raining:
    print("its is not raining dont worry about that")
else:
    print("its is rainig so we have to take umbrellla")



  





