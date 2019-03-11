# -*- coding: utf-8 -*-


#Console IO

inp1 = input("Enter a number : ")
number1 = int(inp1)

inp2 = input("Enter a number : ")
number2 = int(inp2)

print(number1+number2)

#File IO

#Writing to file

inp = input("Enter some text : ")

with open("textfile.txt","a") as f:
    f.write(inp)
    
with open("textfile.txt","r") as f:
    print(f.read())    
