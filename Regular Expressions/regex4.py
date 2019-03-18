# -*- coding: utf-8 -*-
import re

sentence1 = "Welcome to year 2019"
sentence2 = "Just ~% +++--- arrived at @Jack's place. #fun"
sentence3 = "I      love    you"

sentence1_modified = re.sub(r"\d","",sentence1)
print(sentence1_modified)

sentence2_modified = re.sub(r"[%@#~+-\.']","",sentence2)
print(sentence2_modified)

#\w -> removes a-zA-Z0-9
sentence2_modified = re.sub(r"\w"," ",sentence2)
print(sentence2_modified)

#\W -> opposite of w
sentence2_modified = re.sub(r"\W"," ",sentence2)
print(sentence2_modified)

#one or more spaces are replaced by single space
sentence2_modified = re.sub(r"\s"," ",sentence2_modified)
print(sentence2_modified)

#Just arrived at Jack s place fun --- removing the alone 's'
sentence2_modified = re.sub(r"\s+[a-zA-Z]\s+"," ",sentence2_modified)
print(sentence2_modified)

sentence3_modified = re.sub(r"\s+"," ",sentence3)
print(sentence3_modified)


sentence3_modified = re.sub(r"\slove\s","hate",sentence3)
print(sentence3_modified)

sentence3_modified = re.sub(r"\s+love\s+"," hate ",sentence3)
print(sentence3_modified)