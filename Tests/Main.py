from Tests.User import User
import time
# The locations of the Base Stations


# Create 100 users
numberOfUser = 100

# users = [None] * numberOfUser
users = []

# for k in range(0, numberOfUser):
for k in range(0, 3):
    # Create different 10 users
    users.append(User(k))

    print("id = ",users[k].id)
    print("direction = ",users[k].direction)
    print("speed = ",users[k].speed)


print("------------ ------------ ------------ \n")

j = 0
while True:
    if j == 3:
        time.sleep(1)
        j = 0
        print("------------\n")
    # each user is moved for 1 step
    users[j].keepMove()


    # now if the boundary is reached user must be deleted and new user must be assigned
    if users[j].xValue > 10000 or users[j].yValue > 10000 or users[j].xValue < 0 or users[j].yValue < 0:
        del users[j]
#       add a new user
        users.append(User(4))

    j += 1
# k = 0
# while True:
#     users[k].keepMove()
#     print(users[k].id)
#     k += 1
#
# baseStation1 = [0, 5000]
#
# print(baseStation1[1])
#
# user = User(1)
# print(user.getNearestBS())
