import os 
import shutil
#to creat new file:
os.mkdir("c:\\newfile")
#the current path is 
prasentpath = "c:\\pavan\\rajkumar.txt\\SOMESH.txt"
#now copy to this file 
copypath = "c:\\newfile"
#to run this method is to used:
shutil.copy(prasentpath,copypath)