# class parent:
#     name="rakesh"
#     age=98
#     number=8107867656
#     def __init__(self,name,age,number):
#        self.name= name
#        self.age=age
#        self.number=number
# obj=parent("raju",78,83437847384)
# print(obj.name,obj.age,obj.number)


# class child(parent):
#     branch="xyz"
#     salary=70000   
#     def __init__(self, name, age, number):
#         super().__init__(self,name,age,number,)
#         self.branch=branch
#         self.salary=salary

# obj=child("abx",45677)
# print(obj.name,obj.age,obj.number,obj.branch,obj.salary)





# chaild object implimentation
# ===================
class Vechile:
    mileg=50
    capacity=34
    vechile_name="mercedus"
    price=1,23,000
    def _int_(self):
        print("default constructor is called")
    def _init_(self,mileg=80,capcity=34,vechile_name="audi",price=40000):
        self.mileg=mileg
        self.capacity=capcity
        self.vechile_name=vechile_name
        self.price=price
    def display(self):
        print("the details of vechile are:")
        print("vechile name:",self.vechile_name)
        print("vechile price:",self.price)
        print("vechile petrol capcity:", self.capacity)
        print("vechile mileg:",self.mileg)

# mercedusobj = Vechile(67,45,"baleno",90000)
# default_vechile=Vechile()
# mercedusobj.display()
# default_vechile.display()
class Sub_vechile(Vechile):
    engine="SI-Engine"
    chasis_no=23.457
    def _int_(self,engine,chasis_no):
        self.engine=engine
        self.chasis_no=chasis_no

        super(). _init_(self,mileg=80,capcity=34,vechile_name="audi",price=40000)
    def print(self):
        
        print("the details of sub-vechile are:")
        print("vechile name:", self.vechile_name)
        print("vechile price:", self.price)
        print("vechile petrol capcity:", self.capacity)
        print("vechile mileg:", self.mileg)
        print("vechile engine type:",self.engine)
        print("chasis number:",self.chasis_no)
        
childObj = Sub_vechile()
childObj.print()
        
    

       
    

    
    