import random
import bisect
import itertools

from Tests.Time_Loop_Dir.UserTest import User
import time
from Tests.Time_Loop_Dir.BaseStation import BaseStation


# The locations of the Base Stations
class MainTest:
    sizeOfUsers = 99
    sizeUpdated = False
    # Create 100 users
    users = []

    # following baseStation can only have 20 users per each
    distanceFrom_BS1 = []
    distanceFrom_BS2 = []
    distanceFrom_BS3 = []

    usersOf_BS1 = {}
    usersOf_BS2 = {}
    usersOf_BS3 = {}

    countOfBS1 = 0
    countOfBS2 = 0
    countOfBS3 = 0

    def BS_MoveTheUser(self, connected_BS1_user, BS_users):
        connected_BS1_user.keepMove()
        isRemoved = False
        # now if the boundary is reached user must be deleted and new user must be assigned
        if connected_BS1_user.xValue > 10000 or connected_BS1_user.yValue > 10000 or connected_BS1_user.xValue < 0 or connected_BS1_user.yValue < 0:
            BS_users.remove(connected_BS1_user)
            isRemoved = True
            # MainTest.sizeOfUsers += 1
            # newUser = User(MainTest.sizeOfUsers)
            # MainTest.users.append(newUser)
            # print("all users = ", MainTest.sizeOfUsers)
        return isRemoved

    def BS_CallingProcess(self, connected_BS_user, BS_users):
        connected_BS_user.isConnected = True
        connected_BS_user.callDuration = connected_BS_user.setCallDuration()
        connected_BS_user.makeCall()
        # time.sleep(connected_BS1_user.callDuration / 1000)
        connected_BS_user.hangUpTheCall()
        # print("Call ended")
        BS_users.remove(connected_BS_user)
        # isRemoved = True
        # MainTest.sizeOfUsers += 1
        # newUser = User(MainTest.sizeOfUsers)
        # MainTest.users.append(newUser)

    def Diff(self, li1, li2):
        return list(list(set(li1) - set(li2)) + list(set(li2) - set(li1)))

    def addNextUser(self, restOfUserList):
        newUser = restOfUserList[0]
        restOfUserList.remove(restOfUserList[0])
        return newUser

    # def Merge(self, dict1, dict2, dict3):
    #     # res = {**dict1, **dict2, **dict3}
    #     # res = (dict1 | dict2) | dict3
    #     res = dict1.update(dict2)
    #     res = res.update(dict3)
    #     return res

    # for k in range(0, numberOfUser):

    # The simulation will be done for 1000 seconds

    # def merge_three_dicts(self, dict1, dict2, dict3):
    #     """Given two dictionaries, merge them into a new dict as a shallow copy."""
    #     # z1 = x.copy()
    #     # z1.update(y)
    #     # z1.update(z)
    #     res = {**dict1, **dict2, **dict3}
    #     return res


def main():
    mt = MainTest()

    # Setting up the base stations properties
    BS_1 = BaseStation("BS1", 5000, 10000)
    BS_2 = BaseStation("BS2", 0, 0)
    BS_3 = BaseStation("BS3", 10000, 0)

    # All the BS should have same power at each time

    for k in range(0, 100):
        # Create different 10 users
        MainTest.users.append(User(k))

    ts = 0
    power = -35
    # Let's consider 50 seconds
    while ts <= 2:
        power += 5

        BS_1.setThePower(power)
        BS_2.setThePower(power)
        BS_3.setThePower(power)

        maxRadiusOf_BS = BS_1.findMaximumRadius()
        print("max-Radius = ", maxRadiusOf_BS)
        totalNumberOfUsers = 0

        for user in MainTest.users:

            # Classify each user based on the nearest BS with satisfying connection
            if user.nearestBS == "BS1" and user.shortestDistance <= maxRadiusOf_BS:
                # MainTest.distanceFrom_BS1.append(user.shortestDistance)
                # MainTest.usersOf_BS1.append(user)
                MainTest.usersOf_BS1[user] = user.shortestDistance

            if user.nearestBS == "BS2" and user.shortestDistance <= maxRadiusOf_BS:
                # MainTest.distanceFrom_BS2.append(user.shortestDistance)
                MainTest.usersOf_BS2[user] = user.shortestDistance
            if user.nearestBS == "BS3" and user.shortestDistance <= maxRadiusOf_BS:
                # MainTest.distanceFrom_BS3.append(user.shortestDistance)
                MainTest.usersOf_BS3[user] = user.shortestDistance

        # MainTest.distanceFrom_BS1.sort()
        # MainTest.distanceFrom_BS2.sort()
        # MainTest.distanceFrom_BS3.sort()

        # Since each base-station can connect 20 maximum users
        # for (connected_BS1_user, connected_BS2_user, connected_BS3_user) in zip(MainTest.usersOf_BS1[:20],
        #                                                                         MainTest.usersOf_BS2[:20],
        #                                                                         MainTest.usersOf_BS3[:20]):
        #
        #     # Users who connected to Base Station 1
        #     # ----------------------------------------------------------------------------------------------------------
        #     hasRemoved1 = MainTest.BS_MoveTheUser(mt, connected_BS1_user, MainTest.sizeOfUsers, MainTest.usersOf_BS1)
        #     # If the user is in the boundary he is not removed
        #     if ~hasRemoved1:
        #
        #         # print(connected_BS1_user.id, " is calling <BS1 user>")
        #         # MainTest.BS_CallingProcess(mt, connected_BS1_user, MainTest.sizeOfUsers, MainTest.usersOf_BS1)
        #
        #     # ----------------------------------------------------------------------------------------------------------
        #     # Users who connected to Base Station 2
        #     hasRemoved2 = MainTest.BS_MoveTheUser(mt, connected_BS2_user, MainTest.sizeOfUsers, MainTest.usersOf_BS2)
        #     if ~hasRemoved2:
        #         #     continue
        #         # else:
        #         # print(connected_BS1_user.id, " is calling <BS2 user>")
        #         # MainTest.BS_CallingProcess(mt, connected_BS2_user, MainTest.sizeOfUsers, MainTest.usersOf_BS2)
        #
        #     # ----------------------------------------------------------------------------------------------------------
        #     # Users who connected to Base Station 3
        #     hasRemoved3 = MainTest.BS_MoveTheUser(mt, connected_BS3_user, MainTest.sizeOfUsers, MainTest.usersOf_BS3)
        #     if ~hasRemoved3:
        #         #     continue
        #         # else:
        #         # print(connected_BS1_user.id, " is calling <BS3 user>")
        #         # MainTest.BS_CallingProcess(mt, connected_BS3_user, MainTest.sizeOfUsers, MainTest.usersOf_BS3)

        # For SB1
        sorted_tuples = sorted(MainTest.usersOf_BS1.items(), key=lambda item: item[1])
        # print(sorted_tuples)
        sorted_BS1_users = {k: v for k, v in sorted_tuples}

        # For SB2
        sorted_tuples = sorted(MainTest.usersOf_BS2.items(), key=lambda item: item[1])
        # print(sorted_tuples)
        sorted_BS2_users = {k: v for k, v in sorted_tuples}

        # For SB1
        sorted_tuples = sorted(MainTest.usersOf_BS3.items(), key=lambda item: item[1])
        # print(sorted_tuples)
        sorted_BS3_users = {k: v for k, v in sorted_tuples}

        # Extract first 20 users from the three dictionaries into three lists

        sorted_BS1_users20 = list(sorted_BS1_users.keys())[:20]
        sorted_BS2_users20 = list(sorted_BS2_users.keys())[:20]
        sorted_BS3_users20 = list(sorted_BS3_users.keys())[:20]

        # print(w)

        connectedUsers = sorted_BS1_users20 + sorted_BS2_users20 + sorted_BS3_users20
        print("len(connectedUsers): ", len(connectedUsers))
        # Pick 25 users randomly from the connected 60 users
        activeUsers = random.sample(connectedUsers, 25)
        restOfConnectedUsers = mt.Diff(connectedUsers, activeUsers)

        # print(len(restOfConnectedUsers))

        print("Active user count initially: ", len(activeUsers))
        for activeUser in activeUsers:
            hasRemovedFromTheRegion = MainTest.BS_MoveTheUser(mt, activeUser, activeUsers)
            if hasRemovedFromTheRegion:
                activeUsers.append(mt.addNextUser(restOfConnectedUsers))

            # If the user is in the boundary he is not removed
            if ~hasRemovedFromTheRegion:
                # print(activeUser.id, " is calling Active user")
                MainTest.BS_CallingProcess(mt, activeUser, activeUsers)
                activeUsers.append(mt.addNextUser(restOfConnectedUsers))

            activeUser.findInterfering_BaseStations(maxRadiusOf_BS)
            # activeUser.calcInterference(power)
            # activeUser.usefulSignalPower(power)
            radius = BS_1.findMaximumRadius()

            sinr = activeUser.get_SINR(power, radius)
            print("SINR for user ID =", activeUser.id, " = ", sinr)
            if sinr > 1:
                totalNumberOfUsers += 1

        print("Active user count eventually: ", len(activeUsers))

        # continue the timing in the loop
        ts += 1
        print("-------------------------")

    # ___WITHIN 60 USERS RANDOMLY PICK 25 USERS__
    # __ASSIGN THEM A CALL__


if __name__ == '__main__':
    main()
