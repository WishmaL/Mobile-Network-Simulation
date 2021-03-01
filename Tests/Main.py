from Tests.User import User
import time

# The locations of the Base Stations

sizeOfUsers = 2
sizeUpdated = False
# Create 100 users
numberOfUser = 100

# users = [None] * numberOfUser
users = []

# for k in range(0, numberOfUser):
for k in range(0, 3):
    # Create different 10 users
    users.append(User(k))

    print("id = ", users[k].id)
    print("direction = ", users[k].direction)
    print("speed = ", users[k].speed)
    print("Initial location: ", users[k].xValue, users[k].yValue)
    print("\n")
print("------------ ------------ ------------ \n")

j = 0
# while True:
#     # if j == 3:
#     #     time.sleep(0.5)
#     #     j = 0
#     #     print("------------\n")
#
#     # if sizeUpdated:
#     print("Size of the users list: ", len(users))
#
#     # each user is moved for 1 step
#     print("users[j] = ",users[j].id)
#     # users[j].keepMove()
#
#     # now if the boundary is reached user must be deleted and new user must be assigned
#     # if users[j].xValue > 10 or users[j].yValue > 10 or users[j].xValue < 0 or users[j].yValue < 0:
#     #     users.remove(users[j])
#     #     #       add a new user
#     #     sizeOfUsers += 1
#     #     users.append(User(sizeOfUsers))
#     #     sizeUpdated = True
#     #     ADD A FLAG HERE INDICATING THE LIST IS UPDATED
#
#     j += 1
#     if j == 6:
#         break
h = 1
useridx = 0;
while h <= 10:

    # while useridx < len(users):
    for user in users:
        # if sizeUpdated:
        print("Size of the users list: ", len(users))
        print("\n")
        # each user is moved for 1 step
        print("users id = ", user.id)

        user.keepMove()

        # now if the boundary is reached user must be deleted and new user must be assigned
        if user.xValue > 10 or user.yValue > 10 or user.xValue < 0 or user.yValue < 0:
            users.remove(user)
            print("Size of the users list after remove: ", len(users))
            #       add a new user
            print("List updating")
            sizeOfUsers += 1
            users.append(User(sizeOfUsers))
            print("test users id = ", user.id)
            sizeUpdated = True


        # Connect the user to a tower


