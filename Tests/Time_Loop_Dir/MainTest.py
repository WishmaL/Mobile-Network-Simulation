from Tests.User import User
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

    usersOf_BS1 = []
    usersOf_BS2 = []
    usersOf_BS3 = []

    countOfBS1 = 0
    countOfBS2 = 0
    countOfBS3 = 0

    def BS_MoveTheUser(self, connected_BS1_user, sizeOfUsers, BS_users):
        connected_BS1_user.keepMove()
        isRemoved = False
        # now if the boundary is reached user must be deleted and new user must be assigned
        if connected_BS1_user.xValue > 10000 or connected_BS1_user.yValue > 10000 or connected_BS1_user.xValue < 0 or connected_BS1_user.yValue < 0:
            BS_users.remove(connected_BS1_user)
            isRemoved = True
            MainTest.sizeOfUsers += 1
            newUser = User(sizeOfUsers)
            MainTest.users.append(newUser)
            print("all users = ", MainTest.sizeOfUsers)
        return isRemoved

    def BS_CallingProcess(self, connected_BS_user, sizeOfUsers, BS_users):
        connected_BS_user.isConnected = True
        connected_BS_user.callDuration = connected_BS_user.setCallDuration()
        connected_BS_user.makeCall()
        # time.sleep(connected_BS1_user.callDuration / 1000)
        connected_BS_user.hangUpTheCall()
        print("Call ended")
        BS_users.remove(connected_BS_user)
        sizeOfUsers += 1
        newUser = User(sizeOfUsers)
        MainTest.users.append(newUser)

    # for k in range(0, numberOfUser):

    # The simulation will be done for 1000 seconds


def main():
    mt = MainTest()

    # Setting up the base stations properties
    BS_1 = BaseStation("BS1", 0, 5000)
    BS_2 = BaseStation("BS2", 10000, 0)
    BS_3 = BaseStation("BS3", 10000, 10000)

    # All the BS should have same power at each time
    power = -50
    BS_1.setThePower(power)
    BS_2.setThePower(power)
    BS_3.setThePower(power)

    maxRadiusOf_BS1 = BS_1.findMaximumRadius()
    print("max-Radius = ", maxRadiusOf_BS1)
    maxRadiusOf_BS2 = BS_2.findMaximumRadius()
    # print(maxRadiusOf_BS2)
    maxRadiusOf_BS3 = BS_3.findMaximumRadius()
    # print(maxRadiusOf_BS3)

    for k in range(0, 100):
        # Create different 10 users
        MainTest.users.append(User(k))

    ts = 0
    # Let's consider 50 seconds
    while ts <= 20:

        for user in MainTest.users:

            # Classify each user based on the nearest BS
            if user.nearestBS == "BS1":
                MainTest.distanceFrom_BS1.append(user.shortestDistance)
                MainTest.usersOf_BS1.append(user)
            if user.nearestBS == "BS2":
                MainTest.distanceFrom_BS2.append(user.shortestDistance)
                MainTest.usersOf_BS2.append(user)
            if user.nearestBS == "BS3":
                MainTest.distanceFrom_BS3.append(user.shortestDistance)
                MainTest.usersOf_BS3.append(user)

        MainTest.distanceFrom_BS1.sort()
        MainTest.distanceFrom_BS2.sort()
        MainTest.distanceFrom_BS3.sort()

        # Since each base-station can connect 20 maximum users
        for (connected_BS1_user, connected_BS2_user, connected_BS3_user) in zip(MainTest.usersOf_BS1[:20],
                                                                                MainTest.usersOf_BS2[:20],
                                                                                MainTest.usersOf_BS3[:20]):

            # Users who connected to Base Station 1
            # ----------------------------------------------------------------------------------------------------------
            hasRemoved1 = MainTest.BS_MoveTheUser(mt, connected_BS1_user, MainTest.sizeOfUsers, MainTest.usersOf_BS1)
            # If the user is in the boundary he is not removed
            if ~hasRemoved1:
                
                print(connected_BS1_user.id, " is calling <BS1 user>")
                MainTest.BS_CallingProcess(mt, connected_BS1_user, MainTest.sizeOfUsers, MainTest.usersOf_BS1)

            # ----------------------------------------------------------------------------------------------------------
            # Users who connected to Base Station 2
            hasRemoved2 = MainTest.BS_MoveTheUser(mt, connected_BS2_user, MainTest.sizeOfUsers, MainTest.usersOf_BS2)
            if ~hasRemoved2:
                #     continue
                # else:
                print(connected_BS1_user.id, " is calling <BS2 user>")
                MainTest.BS_CallingProcess(mt, connected_BS2_user, MainTest.sizeOfUsers, MainTest.usersOf_BS2)

            # ----------------------------------------------------------------------------------------------------------
            # Users who connected to Base Station 3
            hasRemoved3 = MainTest.BS_MoveTheUser(mt, connected_BS3_user, MainTest.sizeOfUsers, MainTest.usersOf_BS3)
            if ~hasRemoved3:
                #     continue
                # else:
                print(connected_BS1_user.id, " is calling <BS3 user>")
                MainTest.BS_CallingProcess(mt, connected_BS3_user, MainTest.sizeOfUsers, MainTest.usersOf_BS3)

        # continue the timing in the loop
        ts += 1

        # For the graphical representation, take randomly 25 people from the connected people as active (in call
        # state people)
        #
        #     findInterfering_BaseStations need to be called first
        #     calcInterference is next
        #     usefulSignalPower is next
        #     get SINR

    # ___WITHIN 60 USERS RANDOMLY PICK 25 USERS__
    # __ASSIGN THEM A CALL__


if __name__ == '__main__':
    main()
