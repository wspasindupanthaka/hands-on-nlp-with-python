# -*- coding: utf-8 -*-

# list comprehension in Python

numbers1 = [1,2,3,4,5,6,7,8,9,10]

newNumbers1 = []


for number in numbers1:
    newNumbers1.append(number)
    
print(newNumbers1)    


newNumbers2 = [number for number in numbers1]
print(newNumbers2)    


newNumbers3 = [number for number in numbers1 if number <= 5]
print(newNumbers3)   

numbers2 = [1,3,5,7,9]

newNumbers4 = [number for number in numbers1 if number not in numbers2]
print(newNumbers4)   


newNumbers5 = [number*2 for number in numbers1]
print(newNumbers5) 

newNumbers6 = [number for number in numbers1 if number%2==1]
print(newNumbers6)

#Generator comprehension
squareGen = (number**2 for number in numbers1) 
print(list(squareGen))

myDict = {"apple":1,"orange":2,"banana":6}
newDict1 = {key:myDict[key] for key in myDict.keys()}
print(newDict1)

newDict2 = {key:myDict[key] for key in myDict.keys() if myDict[key]>5}
print(newDict2)

words = ["I","Love","Fast & Furious"]
sentence = ' '.join(words)
print(sentence)
