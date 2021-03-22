# import math
# # import Ba
# import random
#
# list1 = []
# list2 = []
# list3 = []
#
# for i in range(1,30,2):
#
#     list1.append(i)
# for i in range(31, 60, 2):
#
#     list2.append(i)
# for i in range(61, 90, 2):
#
#     list3.append(i)
#
# list4 = list1+list2+list3
#
# print(list4)
#
# print(len(list4))
# print("hfjdak hffuaf h")
# print(random.sample(list4, 5))

import bisect

# list1 = [10, 20, 30]
# list1 = []
#
# for i in range(10,1,-1):
#     bisect.insort(list1, i)
#     # bisect.insort(list1, 15)
#
# print(list1)


# dict1 = {1: 1, 2: 9, 3: 4}
# sorted_tuples = sorted(dict1.items(), key=lambda item: item[1])
# print(sorted_tuples)  # [(1, 1), (3, 4), (2, 9)]
# sorted_dict = {k: v for k, v in sorted_tuples}
#
# print(sorted_dict)  # {1: 1, 3: 4, 2: 9}


# def Merge(dict1, dict2, dict3):
#     res = {**dict1, **dict2, **dict3}
#     return res
#
#
# # Driver code
# dict1 = {'a': 10, 'b': 8}
# dict2 = {'d': 6, 'c': 4}
# dict4 = {'e': 7, 'f': 9}
# dict3 = Merge(dict1, dict2, dict4)
# for k in dict3.keys():
#     print(k)

import itertools
import collections

d = collections.OrderedDict((('foo', 'bar'), (1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')))
x = itertools.islice(d.items(), 0, 2)

# for key, value in x:
#     print (key, value)

d = {1: 1, 2: 9, 3: 4}

w = list(d.keys())[:2]
print(w)