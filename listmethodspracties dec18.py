list1 =["nani p","sai","surya",10,11,12,11,"nani",["chanikya","pawan"],13,14,"dhurga",15,"sowjanya",16,11]
print("total list :",list1)
list2=[1,2,3,4,5,6,7]

# example of append method in list :
list1.append(25)
print("after appending 25 value :",list1)

#example of insert method in list :
list1.insert(-5,["vijaya"])
print("after inserting names list :",list1)

list1[-6].insert(1,"sishva")
print("after inserting names list :",list1)

#example of pop() method in list :
list1.pop()
print("after inserting names list :",list1)

#example of pop index method in list :
list1.pop(4)
print("delete the perticular eliment using pop index method :",list1)

#example of extand method in list  :
list1.extend(list2)
print("after extand method the list1 is :",list1)
#example of count method in list :
print(list1.count(11))

#example of remove method in list :
# list1.remove(11)
# print("after deleting the perticular item in a list using romove method :")


# #example of clear method in list :
# list1.clear()
# print("after clearing all eliment in list using clear method :",list1)

# list1.remove(11)
# print("after deleting the perticular item in a list using romove method :")
reverse = list1[::-1]
print("the reversing the list items with  using reverse index:",reverse)