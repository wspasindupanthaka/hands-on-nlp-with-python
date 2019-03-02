# -*- coding: utf-8 -*-


# Break

for i in range(1,11):
    if i>5:
        break;
    print(i)
    i+=1
    
print()

# Continue
for j in range(1,11):
    if j >=4 and j<=7:
        continue;
    print(j)
    j+=1
    

# Pass
k=1
if k==1:
    pass
else:
    pass

#when you dont know what has to be done at the time of writing if statement, then use pass
