# -*- coding: utf-8 -*-
import re

sentence = "I was born in 1992"

#. means any character
#* means 0 or more
print(re.match(r".*",sentence))

#+ means 1 or more 
print(re.match(r".+",sentence))

#[a-zA-z] means only the word characters
print(re.match(r"[a-zA-Z]+",sentence))

sentence = "a"

#checking a and 0 or 1 b 
print(re.match(r"ab?",sentence))