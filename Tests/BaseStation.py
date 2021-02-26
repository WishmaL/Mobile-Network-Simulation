import random


class BaseStation:
    "This is a Base Station class"

    # Add the static variables here

    # def __init__(self, xValue, yValue, isConnected, connectedBase, isInCall, callDuration, speed, direction, dist_BS1, dist_BS2, dist_BS3):
    #     self.xValue = xValue
    #     self.yValue = yValue

    def __init__(self, name, xValue, yValue):

        self.name = name
        self.xValue = xValue
        self.yValue = yValue


