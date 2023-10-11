# class parent:
    
#     def function(self,adress,village,gender):
#         self.adress=adress
#         self.village=village
#         self.gender=gender
#         print(self.adress,self.village,self.gender)

#     def function(self,name,age,gender,adress):
#         self.name=name
#         self.age=age
#         self.gender=gender
#         self.adress=adress
#         print(self.name,self.age,self.gender,self.adress)

# obj=parent()
# obj.function("pavan",78,"male","xyz")
class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("drive")
class boat():
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("somthing")
class plane():
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("plane done")
car1=car("benze","swift")
boat1=boat("big boat","small boat")
plane1=plane("indigo","logical")
for x in (car1,boat1,plane1):
  x.move()
# car1.move()       
# boat1.move()
print("_________________________________________________________________________")
#creat a class called vehicle and make it car,boat,plane are child classes in vehicle;
class vehicle:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def move(self):
        print("movie!")
class car(vehicle):
        pass
class boat(vehicle):
    def move(self):
        print("sahi")
class plane(vehicle):
    def move(self):
        print("different planes")
car1=car("benze",45,89000)
boat1=boat("small ship",433,78000000)
plane1=plane("indigo",6567,56000000)
for x in (car1,boat1,plane1):
    print(x.brand)
    print(x.model)
    print(x.price)
    x.move()
    


        