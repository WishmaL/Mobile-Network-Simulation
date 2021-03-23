import math


class BaseStation:
    "This is a Base Station class"
    n = 2
    baseStation1 = (0, 5000)
    baseStation2 = (10000, 0)
    baseStation3 = (10000, 10000)

    def __init__(self, name, xValue, yValue):
        self.name = name
        self.xValue = xValue
        self.yValue = yValue
        self.power = 0
        self.n = 2

    def setThePower(self, power):
        """Set the power of a base station"""
        self.power = power

    def findMaximumRadius(self):
        """Find the radius that allows to make a call"""
        ty = (self.power + 110) / (10 * self.n)
        return math.pow(10, ty)
