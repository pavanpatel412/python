# private method class
class person:

    def _employedetails(self):
        self.name = input("enter the name:")
        self.age = int(input("enter the age:"))
        self.gender = input("enter the gender:")
        self. _persondetails()

    def _persondetails(self):
     print("details of employee:",self.name,self.age,self.gender)
     
    
obj = person()                      
obj. _employedetails()
print("000000000000000000000000000000000000000000000000000000000000000000000000")
#public method class
class public:
    def employedetails(self):
      self.name=input("enter the name:")
      self.age=int(input("enter the age:"))
      self.gender=input("enter the gender")
      self. persondetails()
    def persondetails(self):
      print("emplooye details is:",self.name,self.age,self.gender)

obj=public()
obj.employedetails()

print("________________________________________")
#private method withot input
class employe_details:
    emp_name = "pavan"
    emp_number = 8106875716
    emp_id = 2434
    emp_role = "developer"
    #defining a function without arguments for employe1 details
    def _selfemploye1(self):
        print("the employe name is:",self.emp_name)
        print("the employe number is:",self.emp_number)
        print("the employe id is:",self.emp_id)
        print("the employe role is:",self.emp_role)
        print("the  details of employe is:",self._persondetails())
    def _persondetails(self): 
        print(self._persondetails)   
obj = employe_details()
obj. _selfemploye1()
      
      