#creating a list

mylists= ["banana", "cherry", "apple"]
print(mylists)


mylists2= [5, True,]
print(mylists2)

#selecting and printing an item

item= mylists[1]
print(item)

#checking if the lists are in the element

for i in mylists:
    print(i)
if "banana" and "cherry" in mylists:
    print("yes")
else:
    print("no")

# checking how much elements are in the list
    
print(len(mylists))

# Adding a new item 

mylists.append("mango")
print(mylists)

# Inserting 

mylists.insert(0, "lemon")
print(mylists)
print(len(mylists))

# Removing an item

item = mylists.pop()
print(item)
print(mylists)

# Delte From anywhere

mylists.__delitem__(0)
print(mylists)
mylists.remove("banana")
print(mylists)

# remove all items

mylists.clear()
print(mylists)

# reversing the lists

mylists= ["banana", "cherry", "apple"]
mylists.reverse()
print(mylists)

# sorting elements

mylists3= [4, 5, 9,-3,-5,-9, 0, 5]
print(mylists3)
new_list= sorted(mylists3)
print(new_list)

# duplicating the same element

mylists4= [7] * 7
print(mylists4)

# adding 2 lists

mylists4= [7] * 7
mylists5= [5] * 5
new_list1= mylists5 + mylists4
print(new_list1)

# start and stop index

v= mylists4[1:5]
print(v) 

# copying from the original list

list_org=["go", "hid", "land"]
list_copy = list_org.copy()
list_copy.append("6")
print(list_copy)
print(list_org)

# squaring
mylists6=[5,4,3,2,1]
s= [i*i for i in mylists6]
print(s)