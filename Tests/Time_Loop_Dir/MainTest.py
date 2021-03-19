from Tests.User import User
import time


# The locations of the Base Stations
class MainTest:
    sizeOfUsers = 29

    # def __init__(self):
    #     MainTest.sizeOfUsers = 29

    # sizeOfUsers = 29  # this indicates the id for newly adding users
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

    def BS_MoveTheUser(self, BS1_user, sizeOfUsers, BS_users):
        BS1_user.keepMove()
        isRemoved = False
        # now if the boundary is reached user must be deleted and new user must be assigned
        if BS1_user.xValue > 10 or BS1_user.yValue > 10 or BS1_user.xValue < 0 or BS1_user.yValue < 0:
            BS_users.remove(BS1_user)
            isRemoved = True
            MainTest.sizeOfUsers += 1
            newUser = User(sizeOfUsers)
            MainTest.users.append(newUser)
            print("all users = ", MainTest.sizeOfUsers)
        return isRemoved

    def BS_CallingProcess(self, connected_BS1_user, sizeOfUsers):
        connected_BS1_user.isConnected = True
        connected_BS1_user.callDuration = connected_BS1_user.setCallDuration()
        connected_BS1_user.makeCall()
        # time.sleep(connected_BS1_user.callDuration / 1000)
        connected_BS1_user.hangUpTheCall()
        MainTest.usersOf_BS1.remove(connected_BS1_user)
        sizeOfUsers += 1
        newUser = User(sizeOfUsers)
        MainTest.users.append(newUser)

    # for k in range(0, numberOfUser):
    for k in range(0, 30):
        # Create different 10 users
        users.append(User(k))

    print("------------ ------------ ------------ \n")

    # The simulation will be done for 1000 seconds


def main():
    ts = 0
    while ts <= 50:

        for user in MainTest.users:

            # Classify each user based on the nearest BS
            if user.nearestBS == "BS1":
                # print("min in BS2")
                MainTest.distanceTo_BS1.append(user.shortestDistance)
                MainTest.usersOf_BS1.append(user)
            if user.nearestBS == "BS2":
                # print("hi")
                MainTest.distanceTo_BS2.append(user.shortestDistance)
                MainTest.usersOf_BS2.append(user)
            if user.nearestBS == "BS3":
                # print("hi")
                MainTest.distanceTo_BS3.append(user.shortestDistance)
                MainTest.usersOf_BS3.append(user)

        MainTest.distanceTo_BS1.sort()
        MainTest.distanceTo_BS2.sort()
        MainTest.distanceTo_BS3.sort()

        for (connected_BS1_user, connected_BS2_user, connected_BS3_user) in zip(MainTest.usersOf_BS1[:10],
                                                                                MainTest.usersOf_BS2[:10],
                                                                                MainTest.usersOf_BS3[:10]):

            # for connected_BS1_user in usersOf_BS1[:10]:
            hasRemoved1 = MainTest.BS_MoveTheUser(connected_BS1_user, MainTest.sizeOfUsers, MainTest.usersOf_BS1)
            if hasRemoved1:
                continue
            else:
                # print("bs1 call")
                MainTest.BS_CallingProcess(connected_BS1_user, MainTest.sizeOfUsers)
            # now if the boundary is reached user must be deleted and new user must be assigned

            hasRemoved2 = MainTest.BS_MoveTheUser(connected_BS2_user, MainTest.sizeOfUsers, MainTest.usersOf_BS2)
            if hasRemoved2:
                continue
            else:
                print("bs2 call")
                MainTest.BS_CallingProcess(connected_BS2_user, MainTest.sizeOfUsers)

            hasRemoved3 = MainTest.BS_MoveTheUser(connected_BS3_user, MainTest.sizeOfUsers, MainTest.usersOf_BS3)
            if hasRemoved3:
                continue
            else:
                print("bs3 call")
                MainTest.BS_CallingProcess(connected_BS3_user, MainTest.sizeOfUsers)

        #
        ts += 1

    # Connect the user to a tower

    # print("countOfBS1", countOfBS1)
    # print("countOfBS2", countOfBS2)
    # print("countOfBS3", countOfBS3)

    # ___WITHIN 60 USERS RANDOMLY PICK 25 USERS__
    # __ASSIGN THEM A CALL__

    if __name__ == '__main__':
        main()
