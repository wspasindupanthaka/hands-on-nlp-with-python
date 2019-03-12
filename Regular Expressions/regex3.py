# -*- coding: utf-8 -*-

import re

sentence = "I love NFS2"

print(re.sub(r"NFS2","NFS6",sentence))


print(re.sub(r"[a-z]","0",sentence))

#Case in-sensitive
print(re.sub(r"[a-z]","0",sentence,flags=re.I))

#Only substitutes the first value
print(re.sub(r"[a-z]","0",sentence,1,flags=re.I))