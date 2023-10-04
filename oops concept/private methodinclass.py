#private method class
class person:

    def _employedetails(self):
        self.name = input("enter the name:")
        self.age = input("enter the age:")
        self.gender = input("enter the gender:")
        self. _persondetails()

    def _persondetails(self):
     print(f"details of employe is:{self.name},{self.age},{self.gender}")
     
    
obj = person()                      
obj. _employedetails()  