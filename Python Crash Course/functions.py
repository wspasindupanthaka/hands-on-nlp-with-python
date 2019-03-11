# -*- coding: utf-8 -*-

def funcName(arg1,arg2):
    print(arg1,arg2)
    
def add(num1,num2):
    return num1+num2
    
funcName("The number is ",125)
print(add(12,90))
print(len([12,15,56]))


def ourOwnLenFunc(l):
    count =0
    for item in l:
        count += 1
    return count