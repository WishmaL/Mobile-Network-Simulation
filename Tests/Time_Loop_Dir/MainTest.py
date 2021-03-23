import random
import time
import matplotlib.pyplot as plt

from Tests.Time_Loop_Dir.UserTest import User
from Tests.Time_Loop_Dir.BaseStation import BaseStation


# The locations of the Base Stations
class MainTest:
    sizeOfUsers = 99
    sizeUpdated = False
    # The 100 users will be stored in users list
    users = []

    # each users distances for each base station will be stored in following lists
    distanceFrom_BS1 = []
    distanceFrom_BS2 = []
    distanceFrom_BS3 = []

    # following baseStation can only have 20 users per each
    usersOf_BS1 = {}
    usersOf_BS2 = {}
    usersOf_BS3 = {}

    # Keep the count of each base station's connected users
    countOfBS1 = 0
    countOfBS2 = 0
    countOfBS3 = 0

    def BS_MoveTheUser(self, connected_BS1_user, BS_users):
        """keep moves the each user"""
        connected_BS1_user.keepMove()
        isRemoved = False
        # now if the boundary is reached user must be deleted and new user must be assigned
        if connected_BS1_user.xValue > 10000 or connected_BS1_user.yValue > 10000 or connected_BS1_user.xValue < 0 or connected_BS1_user.yValue < 0:
            BS_users.remove(connected_BS1_user)
            isRemoved = True
        return isRemoved

    def BS_CallingProcess(self, connected_BS_user, BS_users):
        """Each active user will start call and end the call"""
        connected_BS_user.isConnected = True
        connected_BS_user.callDuration = connected_BS_user.setCallDuration()
        connected_BS_user.makeCall()

        # ___BY UNCOMMENTING FOLLOWING EACH USER WILL SPEND TIME ON CALLING (PROGRAM WILL TAKE MORE TIME )
        # time.sleep(connected_BS1_user.callDuration)

        connected_BS_user.hangUpTheCall()
        # print("Call ended")
        isRemoved = False
        if connected_BS_user in BS_users:
            BS_users.remove(connected_BS_user)
            isRemoved = True
        return isRemoved

    def Diff(self, li1, li2):
        """Get who are the remaining users who are not in call(currently)"""
        return list(list(set(li1) - set(li2)) + list(set(li2) - set(li1)))

    def addNextUser(self, restOfUserList):
        """Add next user to the 'activeUsers' list by removing that user from the 'restOfUserList' list"""
        newUser = restOfUserList[0]
        restOfUserList.remove(restOfUserList[0])
        return newUser

    def getOptimalSignalStrength(self, powerList, activeUsersFreqList):
        """Return the mean signal strength values that give maximum number of active users"""
        idxes = []
        maxValue = max(activeUsersFreqList)
        for i in activeUsersFreqList:
            if i == maxValue:
                idxes.append(activeUsersFreqList.index(i))

        Xvalues = []
        for i in idxes:
            Xvalues.append(powerList[i])

        avg = sum(Xvalues) / len(Xvalues)
        return avg


def main():
    """The main method that runs the whole program"""

    # create an instance of the main method
    mt = MainTest()

    # Setting up the base stations properties
    BS_1 = BaseStation("BS1", 5000, 10000)
    BS_2 = BaseStation("BS2", 0, 0)
    BS_3 = BaseStation("BS3", 10000, 0)

    # All the BS should have same power at each time

    for k in range(0, 100):
        # Create different 100 users at different random locations
        MainTest.users.append(User(k))

    # Initialize the total-number-of-active-users lists and power list
    activeUsersFreqList = []
    powerList = []

    i = 0
    while i <= 0:
        # Following is for plotting purposes
        for power in range(-60, -25, 1):
            totalNumberOfActiveUsers = 0
            powerList.append(power)

            BS_1.setThePower(power)
            BS_2.setThePower(power)
            BS_3.setThePower(power)

            maxRadiusOf_BS = BS_1.findMaximumRadius()

            for user in MainTest.users:

                # Classify each user based on the nearest BS with satisfying connection
                # In each dictionary item, key <= user and value <= distance
                if user.nearestBS == "BS1":
                    MainTest.usersOf_BS1[user] = user.shortestDistance

                if user.nearestBS == "BS2":
                    MainTest.usersOf_BS2[user] = user.shortestDistance

                if user.nearestBS == "BS3":
                    MainTest.usersOf_BS3[user] = user.shortestDistance

            # ___Sort each user with the shortestDistance (according to the value of each item)
            # For SB1
            sorted_tuples = sorted(MainTest.usersOf_BS1.items(), key=lambda item: item[1])
            sorted_BS1_users = {k: v for k, v in sorted_tuples}

            # For SB2
            sorted_tuples = sorted(MainTest.usersOf_BS2.items(), key=lambda item: item[1])
            sorted_BS2_users = {k: v for k, v in sorted_tuples}

            # For SB3
            sorted_tuples = sorted(MainTest.usersOf_BS3.items(), key=lambda item: item[1])
            sorted_BS3_users = {k: v for k, v in sorted_tuples}

            # Extract first 20 users from the three dictionaries into three lists
            sorted_BS1_users20 = list(sorted_BS1_users.keys())[:20]
            sorted_BS2_users20 = list(sorted_BS2_users.keys())[:20]
            sorted_BS3_users20 = list(sorted_BS3_users.keys())[:20]

            # Create a list of all 60 connected users
            connectedUsers = sorted_BS1_users20 + sorted_BS2_users20 + sorted_BS3_users20

            # Randomly 25 users are selected as active users
            activeUsers = random.sample(connectedUsers, 25)
            restOfConnectedUsers = mt.Diff(connectedUsers, activeUsers)

            for activeUser in activeUsers:
                hasRemovedFromTheRegion = MainTest.BS_MoveTheUser(mt, activeUser, activeUsers)
                if hasRemovedFromTheRegion:
                    activeUsers.append(mt.addNextUser(restOfConnectedUsers))

                # If the user is in the boundary (meaning he is not removed)
                if ~hasRemovedFromTheRegion:
                    isCallEnded = MainTest.BS_CallingProcess(mt, activeUser, activeUsers)
                    if isCallEnded:
                        activeUsers.append(mt.addNextUser(restOfConnectedUsers))

                activeUser.findInterfering_BaseStations(maxRadiusOf_BS)
                radius = BS_1.findMaximumRadius()

                sinr = activeUser.get_SINR(power, radius)

                # ___FOR TESTING PURPOSES___

                # print("location: x=", activeUser.xValue, " y=", activeUser.yValue)
                # print("Distance to shortest: ", activeUser.shortestDistance)
                # print("Distance to BS1", activeUser.distanceToBS1)
                # print("Distance to BS2", activeUser.distanceToBS2)
                # print("Distance to BS3", activeUser.distanceToBS3)
                # print("SINR for user ID =", activeUser.id, " = ", sinr)
                # print("\n")
                if sinr >= 1:
                    totalNumberOfActiveUsers += 1
                print("\n")
            print("Active user count: ", totalNumberOfActiveUsers)
            activeUsersFreqList.append(totalNumberOfActiveUsers)
        # continue the timing in the loop
        i += 1
        print("-------------------------")

    # ___PLOTTING___

    plt.plot(powerList, activeUsersFreqList, color='green', linestyle='dashed', linewidth=3,
             marker='o', markerfacecolor='blue', markersize=12)
    # naming the x axis
    plt.xlabel('Base Station Power')
    # naming the y axis
    plt.ylabel('Number of active users')
    # giving a title to the graph
    plt.title('The impact of Signal Strength with the Signal Power')

    # function to show the plot
    plt.show()
    print("\n\n")
    optimal_signal_strength = mt.getOptimalSignalStrength(powerList, activeUsersFreqList)
    print("Optimal Signal Strength = ", optimal_signal_strength)


# __RUN THE MAIN PROGRAMME__
if __name__ == '__main__':
    main()
