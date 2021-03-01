"""Check the capability of appending and removing elements"""

list1 = [12,23,4]
for i in list1:
    print(i)

print("-----------------")
list1.remove(23)
for i in list1:
    print(i)

print("-----------------")
list1.append(56)
for i in list1:
    print(i)
