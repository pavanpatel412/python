import os 
#in w method it can't read it can only write: and it creat new file also
pavan = open("c:\\pavan\\rajkumar.txt\\SOMESH1.txt","w")
# print(pavan.read())
#in w
# on w+ method it can read & write: it can creat new file also.
pavan = open("c:\\pavan\\rajkumar.txt\\SOMESH.txt","w+")
print(pavan.read())
print(pavan.write("nani is toper of the batch"))