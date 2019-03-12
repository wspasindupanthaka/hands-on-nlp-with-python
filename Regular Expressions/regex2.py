# -*- coding: utf-8 -*-
import re

sentence = "I was born in 1992"

print(re.match(r"[a-zA-Z]+",sentence))


sentence = "1992 was the year when I was born"

#why we dont get any response, because match finds only the first pattern in the sentence, none of them matches with the
#given pattern.
print(re.match(r"[a-zA-Z]+",sentence))

#search finds for all the sentence
print(re.search(r"[a-zA-Z]+",sentence))

#Starts with
#^ means the starts with
if re.match(r"^1992",sentence):
    print("Starts with 1992")
else:
    print("Not Starts with 1992")
    
#Ends with
#$ means the ends with
if re.search(r"born$",sentence):
    print("Ends with born")
else:
    print("Not Ends with born")    
