from Tests.User import User
import time

# The locations of the Base Stations

sizeOfUsers = 29  # this indicates the id for newly adding users
sizeUpdated = False
# Create 100 users
# numberOfUser = 100

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
for k in range(0, 30):
    # Create different 10 users
    users.append(User(k))

    # print("id = ", users[k].id)
    # print("direction = ", users[k].direction)
    # print("speed = ", users[k].speed)
    # print("Initial location: ", users[k].xValue, users[k].yValue)
    # print("\n")
#
# print("------------ ------------ ------------ \n")

# Following is need to set True
h = 0
while h <= 6:

    for user in users:

        # Classify each user based on the nearest BS
        if user.nearestBS == "BS1":
            # print("min in BS2")
            distanceTo_BS1.append(user.shortestDistance)
            usersOf_BS1.append(user)
        if user.nearestBS == "BS2":
            # print("hi")
            distanceTo_BS2.append(user.shortestDistance)
            usersOf_BS2.append(user)
        if user.nearestBS == "BS3":
            # print("hi")
            distanceTo_BS3.append(user.shortestDistance)
            usersOf_BS3.append(user)

        # Sort the list in ascending manner
    distanceTo_BS1.sort()
    distanceTo_BS2.sort()
    distanceTo_BS3.sort()

    # get the initial 20 users as the connected users
    for BS1_user in usersOf_BS1:
        if countOfBS1 == 10:  # set 10 to 20
            break
        BS1_user.isConnected = True
        countOfBS1 += 1
        # BS1_user.callDuration = BS1_user.setCallDuration()
        BS1_user.makeCall()
        time.sleep(BS1_user.callDuration / 1000)
        BS1_user.hangUpTheCall()
        usersOf_BS1.remove(BS1_user)
        # usersOf_BS1.append()
        # print(BS1_user.id)

    # print("\n")
    # print("BS2 users")
    for BS2_user in usersOf_BS2:
        if countOfBS2 == 10:
            break
        BS2_user.isConnected = True
        countOfBS2 += 1
        BS2_user.makeCall()
        time.sleep(BS2_user.callDuration / 1000)
        BS2_user.hangUpTheCall()
        usersOf_BS2.remove(BS2_user)
        # print(BS2_user.id)
    #
    # print("\n")
    # print("BS3 users")
    for BS3_user in usersOf_BS3:
        if countOfBS3 == 10:
            break
        BS3_user.isConnected = True
        countOfBS3 += 1
        BS3_user.makeCall()
        time.sleep(BS3_user.callDuration / 1000)
        BS3_user.hangUpTheCall()
        usersOf_BS3.remove(BS3_user)

    # ___Consider usersOf_BS1, usersOf_BS2, usersOf_BS3 for main calc___
    # get the initial 20 users as the connected users

    # ___This Handles the moving users' behaviour___
    for user in users:
        # if sizeUpdated:
        # print("Size of the users list: ", len(users))
        # print("\n")
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

    #
    h += 1
# Connect the user to a tower


# print("countOfBS1", countOfBS1)
# print("countOfBS2", countOfBS2)
# print("countOfBS3", countOfBS3)


# ___WITHIN 60 USERS RANDOMLY PICK 25 USERS__
# __ASSIGN THEM A CALL__