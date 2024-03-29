import random
import time
import math


class User:
    """This is a User class"""

    # Add the static variables here
    # baseStation1 = [0, 5000]
    # baseStation2 = [10000, 0]
    # baseStation3 = [10000, 10000]
    baseStation1 = [5000, 10000]
    baseStation2 = [0, 0]
    baseStation3 = [10000, 0]
    # Noise
    N = -1

    # def __init__(self, xValue, yValue, isConnected, connectedBase, isInCall, callDuration, speed, direction,
    # dist_BS1, dist_BS2, dist_BS3): self.xValue = xValue self.yValue = yValue

    def __init__(self, _id):
        xValue, yValue = self.generateLocation()
        self.xValue = xValue
        self.yValue = yValue
        #
        # self.xValue = 6610
        # self.yValue = 8114

        self.id = _id
        self.speed = self.setSpeed()
        self.direction = self.setDirection()
        self.isConnected = False
        self.isInCall = False
        self.callDuration = 0
        self.nearestBS = self.getNearestBS()[0]
        self.shortestDistance = self.getNearestBS()[1]
        self.distanceToBS1 = 0
        self.distanceToBS2 = 0
        self.distanceToBS3 = 0
        self.interfering_BS_list = set()
        # self.SINR = 0

    # return the location randomly
    def generateLocation(self):
        x = random.randint(0, 10000)
        y = random.randint(0, 10000)
        return x, y

    def setSpeed(self):
        """user can be not move or move; if moves the speed is denoted in m/seconds"""
        speed = random.randint(1, 4)
        return speed

    def setCallDuration(self):
        """set the call duration from 60 to 300 milli-seconds"""
        callTime = random.randint(60, 300)
        return callTime

    def setDirection(self):
        """Randomly pick the direction"""
        direction = ["up", "down", "left", "right"]
        theDir = direction[random.randint(0, 3)]
        return theDir

    def keepMove(self):
        """Move the user until it reaches the boundary of the area"""
        #         go to up direction
        if self.direction == "up":
            self.yValue += self.speed
            # print("User ID = ", self.id, " location: ", self.xValue, self.yValue)
        #         go to down direction
        elif self.direction == "down":
            self.yValue -= self.speed
            # print("User ID = ", self.id, " location: ", self.xValue, self.yValue)

        #         go to left direction
        elif self.direction == "left":
            self.xValue -= self.speed
            # print("User ID = ", self.id, " location: ", self.xValue, self.yValue)

        #         go to right direction
        elif self.direction == "right":
            self.xValue += self.speed
            # print("User ID = ", self.id, " location: ", self.xValue, self.yValue)

        # Calc the distance

    def getDistance(self, baseStation):
        return (((baseStation[0] - self.xValue) ** 2) + ((baseStation[1] - self.yValue) ** 2)) ** 0.5

    def getNearestBS(self):
        """Get the shortest distance and the nearest tower"""
        # From base station 1
        self.distanceToBS1 = self.getDistance(self.baseStation1)
        self.distanceToBS2 = self.getDistance(self.baseStation2)
        self.distanceToBS3 = self.getDistance(self.baseStation3)

        minDistance = min(self.distanceToBS1, self.distanceToBS2, self.distanceToBS3)

        if minDistance == self.distanceToBS1:
            # print("min in BS1")
            connectedBS = "BS1"
        elif minDistance == self.distanceToBS2:
            # print("min in BS2")
            connectedBS = "BS2"
        else:
            connectedBS = "BS3"
        self.isConnected = True
        return connectedBS, minDistance

    # ___Call related calculations___

    def makeCall(self):
        self.isInCall = True
        self.callDuration = self.setCallDuration()

    def hangUpTheCall(self):
        self.isInCall = False
        self.callDuration = 0

    # ___Power related calculations___

    # For following methods the BS_power is equal for each base station
    def getPowerAccordingToDistance(self, distance, BS_power):
        # Here the  constant is taken as 1
        pathLoss = (10 * 2 * math.log(distance, 10)) + 0
        return BS_power - pathLoss

    def usefulSignalPower(self, BS_power):
        """Calculate the useful signal power"""
        distance_ = self.shortestDistance
        # Here the  constant is taken as 1
        pathLoss = (10 * 2 * math.log(distance_, 10)) + 0
        return BS_power - pathLoss

    def findInterfering_BaseStations(self, Max_BS_radius):

        self.distanceToBS1 = self.getDistance(self.baseStation1)
        self.distanceToBS2 = self.getDistance(self.baseStation2)
        self.distanceToBS3 = self.getDistance(self.baseStation3)

        if self.nearestBS == "BS1":
            if self.distanceToBS2 < Max_BS_radius:
                # print("inside BS1, distance to BS2= ", self.distanceToBS2)
                self.interfering_BS_list.add("BS2")
            if self.distanceToBS3 < Max_BS_radius:
                self.interfering_BS_list.add("BS3")
        if self.nearestBS == "BS2":
            if self.distanceToBS1 < Max_BS_radius:
                self.interfering_BS_list.add("BS1")
            if self.distanceToBS3 < Max_BS_radius:
                self.interfering_BS_list.add("BS3")
        if self.nearestBS == "BS3":
            if self.distanceToBS1 < Max_BS_radius:
                self.interfering_BS_list.add("BS1")
            if self.distanceToBS2 < Max_BS_radius:
                self.interfering_BS_list.add("BS2")

    def calcInterference(self, BS_power, radius):
        """Calculate the total interference"""

        self.distanceToBS1 = self.getDistance(self.baseStation1)
        self.distanceToBS2 = self.getDistance(self.baseStation2)
        self.distanceToBS3 = self.getDistance(self.baseStation3)

        totalInterference = 0
        self.findInterfering_BaseStations(radius)

        # print("len of interfering_BS_list: ", len(self.interfering_BS_list))
        # print("Total interfering list is displays below")
        # for i in self.interfering_BS_list:
        # print("BaseStation Name: ",i)

        if "BS1" in self.interfering_BS_list:
            totalInterference += self.getPowerAccordingToDistance(self.distanceToBS1, BS_power)
        if "BS2" in self.interfering_BS_list:
            totalInterference += self.getPowerAccordingToDistance(self.distanceToBS2, BS_power)
        if "BS3" in self.interfering_BS_list:
            totalInterference += self.getPowerAccordingToDistance(self.distanceToBS3, BS_power)

        # if "BS1" or "BS2" or "BS3" not in self.interfering_BS_list:
        # print("Total interference: ", totalInterference)
        return totalInterference + self.N

    def get_SINR(self, BS_power, radius):
        # print("radius: ", radius)
        """FI the SINR > 1 then the call can be made"""
        useful_signal_power = self.usefulSignalPower(BS_power)
        # if useful_signal_power >= -110:
        #     SINR = useful_signal_power / self.calcInterference(BS_power, radius)
        # else:
        #     SINR = 0

        SINR = useful_signal_power / self.calcInterference(BS_power, radius)

        return SINR
