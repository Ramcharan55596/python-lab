#B7. Identity Operators
#Operators: is , is not
#Task B7.1: Create two lists with the same content, list1 and list2, and a third variable list3 = list1.
#Use the is and is not operators (along with id()) to check and explain which variables refer to the same
#object in memory.
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print(list1 == list2) 
print(list1 is list2)  
print(list1 is list3) 
print(id(list1), id(list2), id(list3))

#output
#True
#False
#True
#1341215917440 1341179297472 1341215917440
