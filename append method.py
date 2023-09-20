import os 
#in a method it can't read it can only write: and it creat new file also
# pavan = open("c:\\pavan\\rajkumar.txt\\SOMESH2.txt","a")
# print(pavan.read())
# in a+ method it can read & write: it can creat new file also.
pavan = open("c:\\pavan\\rajkumar.txt\\SOMESH3.txt","a+")
print(pavan.read())
print(pavan.write("nani is toper of the batch"))