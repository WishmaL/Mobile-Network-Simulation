mylist = [0, 1, 2, 3, 4, 5, 6]

print(mylist)
# for i in mylist:
#
#     print(i)
#     print(mylist.)
#     if i == 2:
#         mylist.remove(2) i=0





for i in range(0, len(mylist)):
    print("i=", i)
    print(mylist[i])

    if mylist[i] == 2:
        mylist.remove(mylist[i])
        mylist.append(100)
        print("new elemnt =",mylist[i])
        print("---------")

# mylist.remove(2)
# mylist.remove(3)
# print(mylist)
