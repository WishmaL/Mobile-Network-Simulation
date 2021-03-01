# baseStation1 = (0, 5000)
# baseStation2 = (10000, 0)
# baseStation3 = (10000, 10000)
#
# print(baseStation1[1])

# for k in range(0, 3):
#     print(k)
from itertools import cycle

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
