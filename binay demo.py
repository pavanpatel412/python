import os 
import pickle
# os.mkdir("c:\\mypythonfile")
os.chdir("c:\\mypythonfile")
file1 = open("c:\\mypythonfile\\Binaryfile1.dat","ab+")
binaryfile = {"one","two","three","two","somesh","pavan"}
binarydata = {1:"nani",2:"sai",3:"kumar"}

pickle.dump(binaryfile,file1)
file1.seek(0,0)
output = pickle.load(file1)
print(output)
print('THE POSITION OF THE CURRENT CURSOR IS:',file1.tell())

pickle.dump(binarydata,file1)
file1.seek(53,0)
output= pickle.load(file1)
print(output)
print("current cursor position is:",file1.tell())



