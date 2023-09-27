#creating employe details class
class employe_details:
    emp_name = "pavan"
    emp_number = 8106875716
    emp_id = 2434
    emp_role = "developer"
#defining a function without arguments for employe1 details
    def selfemploye1(self):
        print("the employe name is:",self.emp_name)
        print("the employe number is:",self.emp_number)
        print("the employe id is:",self.emp_id)
        print("the employe role is:",self.emp_role)
#defining a function without arguments for employe2 details
    def selfemploye2(self):
          print("the employe name is:",self.emp_name)
          print("the employe number is:",self.emp_number)
          print("the employe id is:",self.emp_id)
          print("the employe role is:",self.emp_role)
#defining a function with arguments for employe3 details
    def selfemploye3(self,name,number,id,role):
        self.name = name
        self.number = number
        self.id = id
        self.role = role
        print("the employe name is:",self.name)
        print("the employe number is:",self.number)
        print("the employe id is:",self.id)
        print("the employe role is:",self.role)
         
      
#creating object for cAlling the employe class
Employe_details = employe_details()
#calling employe1 function with in the class
Employe_details.selfemploye1()
print("---------------")
#ubtating the defualt employe details
Employe_details.emp_name= "nani"
Employe_details.emp_id = 2345
Employe_details.emp_number = 986754657
Employe_details.emp_role = "fullstock developer"
#calling employe2 function ofter ubdating the defualt details
Employe_details.selfemploye2()

print("------------------")
#calling the employe3 function with passing the parameters
Employe_details.selfemploye3("raju",8886728283,456,"video mixing")
