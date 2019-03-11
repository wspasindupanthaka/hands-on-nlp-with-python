# -*- coding: utf-8 -*-

#Same as list, but immutable

tuple1 = (12,"Simple string",13.8,"Another simple string")

print(tuple1)

print(tuple1[0])

tuple2 = (50,90,2)

tuple3 = tuple1 + tuple2

print(tuple3)

print("Tuple3 length ",len(tuple3))

for i in range(0,len(tuple3)):
    print(tuple3[i])

print()
print()

for item in tuple3:
    print(item)