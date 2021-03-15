import threading

from Tests.User import User
import time

# import itertools

sizeOfUsers = 49

distanceTo_BS1 = []
# distanceTo_BS2 = []
# distanceTo_BS3 = []

usersOf_BS1 = []
# usersOf_BS2 = []
# usersOf_BS3 = []

countOfBS1 = 0
# countOfBS2 = 0
# countOfBS3 = 0

users = []

for k in range(0, 50):
    # Create different 10 users
    users.append(User(k))

h = 0


def BS1_MoveTheUser(BS1_user, sizeOfUsers):
    BS1_user.keepMove()
    isRemoved = False
    # now if the boundary is reached user must be deleted and new user must be assigned
    if BS1_user.xValue > 10 or BS1_user.yValue > 10 or BS1_user.xValue < 0 or BS1_user.yValue < 0:
        usersOf_BS1.remove(BS1_user)
        isRemoved = True
        sizeOfUsers += 1
        newUser = User(sizeOfUsers)
        users.append(newUser)
        # print("test users id = ", user.id)
    return isRemoved


def BS1_CallingProcess(connected_BS1_user, sizeOfUsers):
    connected_BS1_user.isConnected = True
    connected_BS1_user.callDuration = connected_BS1_user.setCallDuration()
    connected_BS1_user.makeCall()
    # time.sleep(connected_BS1_user.callDuration / 1000)
    connected_BS1_user.hangUpTheCall()
    usersOf_BS1.remove(connected_BS1_user)
    sizeOfUsers += 1
    newUser = User(sizeOfUsers)
    users.append(newUser)


while h <= 5:
    for user in users:

        # Classify each user based on the nearest BS
        if user.nearestBS == "BS1":
            distanceTo_BS1.append(user.shortestDistance)
            usersOf_BS1.append(user)

    distanceTo_BS1.sort()

    for connected_BS1_user in usersOf_BS1[:10]:
        hasRemoved = BS1_MoveTheUser(connected_BS1_user, sizeOfUsers)
        if hasRemoved:
            continue
        else:
            print("hrrl")
            BS1_CallingProcess(connected_BS1_user, sizeOfUsers)
        # now if the boundary is reached user must be deleted and new user must be assigned

    #
    h += 1
