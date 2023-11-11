# set is unordered 
names = {"pavan","raju","somesh","kiran","sai"}
names2 = {"dora","nani","cherry"}
names3 = {"raju","kiran","pavan"}
print(names)
names.add("dora")
print(names)
names.pop()
print(names)
names.discard("dora")
print(names)


# ==================//
names4 = {"pavan","raju","somesh","kiran","sai"}
names5 = {"kiran","dora","nani","cherry"}
names6 = {"raju","kiran","pavan"}
print("intersection of the names4 and names5 :",names4.intersection(names5))
print("difference between the names4 and names5 :",names4.difference(names5))
print(names6)
print("difference between the names4 and nams5: ",names4.difference(names5))
# names5.difference_update(names4)
print(names5)
print("names4 is super set of namees6 ;",names4.issuperset(names6))
print(names4.isdisjoint(names5))
names5.intersection_update(names6)
print(names5)


