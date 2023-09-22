# import os
# import shutil
#write a program to find grade in student qualification 
#input student details 
def add_student():
    student_name = input("enter student name:")
    student_id = input("enter student  id:")
    student_class = input("enter student class:")
    subject1_marks = int(input("enter the subject1 marks:"))
    subject2_marks = int(input("enter the subject2 marks"))
    subject3_marks = int(input("enter the subject3 marks"))
    student_grade = ""
    #caluclate the total and percentage
    Total = subject1_marks+subject2_marks+subject3_marks
    per = Total/3
    #caluclate the grade based on percentage
    if per>=90:
            student_grade = "A+"
    elif per>=80:
            student_grade = "A" 
    elif per>= 70:
            student_grade =  "B+"
    elif per>=60:
            student_grade = "B"
    elif per>=50:
            student_grade = "c"
    else:
            "fail"
            #enter formate
    student_data = f"student name is:{student_name}\n"\
                     f"student id is:{student_id}\n"\
                     f"student class is:{student_class}\n"\
                     f"subject1 marks is:{subject1_marks}\n"\
                     f"subject2 marks is :{subject2_marks}\n"\
                     f"sunject3 marks is:{subject3_marks}\n"\
                     f"student grade is:{student_grade}\n"\
                     f"percentage is:,{per}\n"
#open file in the c drive in pavan file 
    file1 = open("c:\\pavan\\rajkumar.txt\\SOMESH52.txt","a")
    file1.write(student_data)
    file1.close()
    print("the student data has been added successusfully!")
#now iterate using while 
def main():
    while True:
       
        print("enter 1 to itarate ")
        print("enter 2 to stop")

        enter = input("to enter some number:")
    
        if  enter =="1":
            add_student()
        elif enter == "2":
             break
        else:
         print("you entered wrong number try again")
            
main()
    

    

