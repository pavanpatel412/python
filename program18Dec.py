# SIMPLE PROGRAM... FOR PRACTIES
# sum = 0
# for i in range(2,18,2):
#     sum += i >sum
# print(sum)
# Take 10 integers from keyboard using loop and print their average value on the screen.
numbers = []
for i in range(10):
  num = int(input("enter some integer:"))
  numbers.append(num)
total_numbers = sum(numbers)
avarage = total_numbers/10
print("average is:",avarage)  
# using while looop
some = 0
i = 10
while i>0:
    num1= int(input("enter some integer:"))
    some +=num1
    i = i-1
avaragenum = some/10
print(avaragenum)