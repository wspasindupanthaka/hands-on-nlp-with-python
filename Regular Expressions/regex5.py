# -*- coding: utf-8 -*-

import re

X = ["This is a wolf scary",
     "Welcome to jungle #missing",
     "11322 the number to know",
     "Remember the name s - john",
     "I    love   you"]


for i in range(len(X)):
    X[i] = re.sub(r"\W"," ",X[i]) #removed all non-wording characters
    X[i] = re.sub(r"\d"," ",X[i]) #removed all digit characters
    X[i] = re.sub(r"\s+[a-z]\s"," ",X[i],flags=re.I) #removed all single characters
    X[i] = re.sub(r"\s+"," ",X[i]) #removed all unnecessary spaces
    X[i] = re.sub(r"^\s+","",X[i]) #removed starting space, if sentence is started with space
    X[i] = re.sub(r"\s$","",X[i]) #removed ending space, if sentence is ended with space