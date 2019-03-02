
#Non homegeneos list
list1 = [12,12.1,"Hi"]


#Printing a list

print(list1)

print(list1[0])
print(list1[1])

#Inserting elements

list1.append(15)
print(list1)

list1.insert(0,"Inserted")
print(list1)


#Updating list

list1[0]=125

print(list1)


#Delete element
list1.pop()
print(list1)

del list1[2]
print(list1)