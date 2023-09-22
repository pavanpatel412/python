import os
import shutil
#write a program to print student details in the text file
#input student details
def add_student():
    student_name = input("enter student name:")
    student_id = input("enter student  id:")
    student_grade = input("enter student grade:")
    marks = input("enter the student marks:")
    student_class = input("enter student class:")

    student_data = f"({student_name},{student_id},{student_grade},{marks},{student_class})\n"
#open a file in the c drive using append method
    file1 = open("c:\\pavan\\rajkumar.txt\\SOMESH51.txt","a")
    file1.write(student_data)
    file1.close()
    print("the student data has been added successusfully!")
#now iterate using while loop 
def main():
    while True:
        print("1.iterate to add student")
        print("2.exit")

        choice = input("to choose one number:")
    
        if  choice =="1":
            add_student()
        elif choice == "2":
             break
        else:
            print("invalid choice.please try again")

main()
    

    

