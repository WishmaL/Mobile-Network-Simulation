import random
import time


class User:
    """This is a User class"""

    # Add the static variables here
    baseStation1 = [0, 5000]
    baseStation2 = [10000, 0]
    baseStation3 = [10000, 10000]

    # def __init__(self, xValue, yValue, isConnected, connectedBase, isInCall, callDuration, speed, direction, dist_BS1, dist_BS2, dist_BS3):
    #     self.xValue = xValue
    #     self.yValue = yValue

    def __init__(self, id):
        xValue, yValue = self.generateLocation()
        self.xValue = xValue
        self.yValue = yValue
        self.id = id
        self.speed = self.setSpeed()
        self.direction = self.setDirection()
        self.isConnected = False
        self.callDuration = 0

    # return the location randomly
    def generateLocation(self):
        x = random.randint(0, 10000)
        y = random.randint(0, 10000)
        return x, y

    def setSpeed(self):
        """user can be not move or move; if moves the speed is denoted in m/seconds"""
        speed = random.randint(0, 6)
        return speed

    def setCallDuration(self):
        """set the call duration from 60 to 300 seconds"""
        callTime = random.randint(60, 300)
        return callTime

    def setDirection(self):
        """Randomly pick the direction"""
        direction = ["up", "down", "left", "right"]
        dir = direction[random.randint(0, 3)]
        return dir

    def keepMove(self):
        """Move the user until it reaches the boundary of the area"""
        #         go to up direction
        if self.direction == "up":
            while self.yValue < 10000:
                self.yValue += self.speed
                time.sleep(1)
                print(self.xValue, self.yValue)
        #         go to down direction
        elif self.direction == "down":
            while self.yValue > 0:
                self.yValue -= self.speed
                time.sleep(1)
                print(self.xValue, self.yValue)

        #         go to left direction
        elif self.direction == "left":
            while self.xValue > 0:
                self.xValue -= self.speed
                time.sleep(1)
                print(self.xValue, self.yValue)

        #         go to right direction
        elif self.direction == "right":
            while self.xValue > 0:
                self.xValue += self.speed
                time.sleep(1)
                print(self.xValue, self.yValue)

        # Calc the distance

    def getDistance(self, baseStation):
        return (((baseStation[0] - self.xValue) ** 2) + ((baseStation[1] - self.yValue) ** 2)) ** 0.5

    def getNearestBS(self):
        # From base station 1
        distance1 = self.getDistance(self.baseStation1)
        distance2 = self.getDistance(self.baseStation2)
        distance3 = self.getDistance(self.baseStation3)

        minDistance = min(distance1, distance2, distance3)
        print(distance1, distance2, distance3)
        print(minDistance)

        if minDistance == distance1:
            connectedBS = self.baseStation1
        elif minDistance == distance2:
            connectedBS = self.baseStation2
        else:
            connectedBS = self.baseStation3
        self.isConnected = True
        return connectedBS

    def makeCall(self):
        self.callDuration = self.setCallDuration()

#   now the user must connect tot he nearest tower
