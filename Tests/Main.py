from Tests.User import User
import time

# The locations of the Base Stations

sizeOfUsers = 2
sizeUpdated = False
# Create 100 users
numberOfUser = 100

# users = [None] * numberOfUser
users = []

# following baseStation can only have 20 users per each
distanceTo_BS1 = []
distanceTo_BS2 = []
distanceTo_BS3 = []

usersOf_BS1 = []
usersOf_BS2 = []
usersOf_BS3 = []

countOfBS1 = 0
countOfBS2 = 0
countOfBS3 = 0

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

h = 1
while h <= 10:

    # ___
    for user in users:
        # Classify each user based on the nearest BS
        if user.nearestBS == "BS1":
            distanceTo_BS1.append(user.shortestDistance)
            usersOf_BS1.append(user)
        if user.nearestBS == "BS2":
            distanceTo_BS2.append(user.shortestDistance)
            usersOf_BS2.append(user)
        if user.nearestBS == "BS3":
            distanceTo_BS3.append(user.shortestDistance)
            usersOf_BS3.append(user)

        # Sort the list ascendingly
        distanceTo_BS1.sort()
        distanceTo_BS2.sort()
        distanceTo_BS3.sort()

    # set as connected for the first 20 users

    # ___Consider usersOf_BS1, usersOf_BS2, usersOf_BS3 for main calc___
    for BS1_user in usersOf_BS1:
        if countOfBS1 == 20:
            break
        BS1_user.isConnected = True
        countOfBS1 += 1

    for BS2_user in usersOf_BS2:
        if countOfBS2 == 20:
            break
        BS2_user.isConnected = True
        countOfBS2 += 1

    for BS3_user in usersOf_BS3:
        if countOfBS3 == 20:
            break
        BS3_user.isConnected = True
        countOfBS3 += 1

    # ___This Handles the moving users' behaviour___
    for user in users:
        # if sizeUpdated:
        # print("Size of the users list: ", len(users))
        print("\n")
        # each user is moved for 1 step
        # print("users id = ", user.id)
        user.keepMove()

        # now if the boundary is reached user must be deleted and new user must be assigned
        if user.xValue > 10 or user.yValue > 10 or user.xValue < 0 or user.yValue < 0:
            users.remove(user)
            # print("Size of the users list after remove: ", len(users))
            #       add a new user
            # print("List updating")
            sizeOfUsers += 1
            newUser = User(sizeOfUsers)
            users.append(newUser)
            # print("test users id = ", user.id)
            sizeUpdated = True

            # assign the next user for that base Station
            if sizeUpdated:
                if newUser.nearestBS == "BS1":
                    distanceTo_BS1.append(newUser.shortestDistance)
                    usersOf_BS1.append(newUser)
                if newUser.nearestBS == "BS2":
                    distanceTo_BS2.append(newUser.shortestDistance)
                    usersOf_BS2.append(newUser)
                if newUser.nearestBS == "BS3":
                    distanceTo_BS3.append(newUser.shortestDistance)
                    usersOf_BS3.append(newUser)

                distanceTo_BS1.sort()
                distanceTo_BS2.sort()
                distanceTo_BS3.sort()

                sizeUpdated = False
        #
    h += 1
    # Connect the user to a tower
