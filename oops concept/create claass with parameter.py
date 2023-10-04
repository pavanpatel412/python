# #if u missing one updated value then u get some output is like ur missing some agrument
# class class1:
#     name="pavan"
#     age=29
#     gender="male"
    
#     def  __init__(self,name,age,gender):
#        self.name=name
#        self.age=age
#        self.gender=gender
# obj=class1("somesh",46,)
# print(obj.name,obj.age,obj.gender)
# print("--------------------------------")


# if u not missing the argument to get output properly..

class class1:
    name="pavan"
    age=29
    gender="male"
    
    def  __init__(self,name,age,gender):
       self.name=name
       self.age=age
       self.gender=gender
obj=class1("raju",46,"male")
print(obj.name,obj.age,obj.gender)

#to assign some values  in init function...
class class1:
    name="pavan"
    age=29
    gender="male"
    
    def  __init__(self,name="sanju",age=56,gender="male"):
       self.name=name
       self.age=age
       self.gender=gender
obj=class1("ramu",47,"male")
print(obj.name,obj.age,obj.gender)



