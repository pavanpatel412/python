# A student will not be allowed ti sit in exams if his/her attendence is less than 75% take a following input from user
# Number of classes held Numbwe of classes attended. and print
# and print  percentage of class attended is student  is allowed to sit in exam or not/.
# noh = int(input("Number of classes held;"))
# noa = int(input("Number of classes attended:"))
# atten = (noa/float(noh))*100
# print("attendence is :",atten)
# if atten >=75:
#     print("you are allowed to sit in exams")
# else:
#     print("sorry your not allowed to sit in exams>>")

# # Modify the above question to allow student to sit if he/she has medical cause or not ("y" or "n") and print accordingly.
# noh = int(input("Number of classes held;"))
# noa = int(input("Number of classes attended:"))
# atten = (noa/float(noh))*100
# print("attendence is :",atten)
# medical_cause = str(input("if he/she has any medical causes:"))
# if (medical_cause) == "Yes":
#     print("due to medical_cause, he/she is allowed to attend the examination hall")
# else:
#     if atten>=75:
#        print("you are allowed to sit in exams")
#     else:
#        print("sorry your not allowed to sit in exams>>")
def multiplication_or_sum(num1,num2):
    if (num1*num2)<=1000:
        return(num1*num2)
    else:
        return (num1+num2)
newobj = multiplication_or_sum(40,20)
print("the calculation of two numbers is:",newobj)

# print the sum of the current number and the previous number:
previous_number = 0
for i in range(1,11):
  previous_number = 0+i
  x_sum = previous_number+i
  print("the current number is ;",i,"previous number is;",previous_number,"sum of the previous number and current number is:",x_sum )
