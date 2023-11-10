#runt time error 
# value error.....
try:
    number = int(input("enter the number:"))
    print(number*2)
except ValueError :
    print("enter the number not a string;")

# logic error example..........//
try:
   numbers = [5,6,7,7,88,8]
   result = numbers+sum
   print(result)
except :
    print("logic error;")
    numbers = [5,6,7,7,88,8]
    result = sum(numbers)
    print(result)