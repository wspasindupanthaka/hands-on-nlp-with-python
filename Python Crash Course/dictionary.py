

# Key - value pairs

dict1 =  {}

#Adding elements to dictionary

dict1['apple'] = "Apple is a fruit"
dict1['orange'] = "Orange is a fruit"
dict1['priusc'] = "Prius C is a car"
dict1['python'] = "Python is a language"
dict1['list'] = [12,12.1,"Hi"]

print(dict1)
print(dict1['apple'])
print(dict1['orange'])
print(dict1['list'])

print()
# The difference here is, if the key is not there the specified default value is printed 
print(dict1.get("apple1",'Key not exists'))


#To delete
del dict1['apple']

print(len(dict1))

print()

#Get keylist
listOfKeys = list(dict1.keys())
print(listOfKeys)

#Get values list
listOfValues = list(dict1.values())
print(listOfValues)


#Iterating

print()

for key in dict1.keys():
    print(dict1[key])

