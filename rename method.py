import os 
import shutil
#to creat new file:
# os.mkdir("c:\\newfile")
#the current path is 
prasentpath = "c:\\pavan\\rajkumar.txt\\SOMESH1.txt"
#now copy to this file 
copypath = "c:\\newfile\\nani2.txt"
#to run this method is to used:
os.rename(prasentpath,copypath)