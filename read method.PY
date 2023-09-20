import os 
#to read the existing file but does not a creat new file 
pavan = open("c:\\pavan\\rajkumar.txt\\SOMESH.txt","r")
print(pavan.read())
#to write somthing statement in the excisting file:
pavan = open("c:\\pavan\\rajkumar.txt\\SOMESH.txt","r+")
print(pavan.read())
print(pavan.write("hello python"))