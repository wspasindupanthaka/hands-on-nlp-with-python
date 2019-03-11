
#Non homegeneos list
list1 = [12,12.1,"Hi"]


#Printing a list

print(list1)

print(list1[0])
print(list1[1])

print()

#Inserting elements

list1.append(15)
print(list1)

list1.insert(0,"Inserted")
print(list1)

print()


#Updating list

list1[0]=125

print(list1)

print()


#Delete element
list1.pop()
print(list1)

del list1[2]
print(list1)

<<<<<<< HEAD
print()

#List length
print(len(list1))

print()

#List Iterating

for index in range(0, len(list1)):
    print(list1[index])
    
print()
    
for item in list1:
    print(item)    
=======
for index in range(0,len(list1)):
    print(list1[index], end=",")
    
print()
print()
    
for item in list1:
    print(item)
>>>>>>> f284e7678be47171f81172b6382c64cf93a99a24
