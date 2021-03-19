from Tests.Main import users
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
    # Sample power values = 10^-11 to 10^1 ,with odd power values

    def setThePower(self, power):
        self.power = power

    # Let's find the radius
    #     def findRadius(self):
    #         """unit: meters"""
    #         return math.sqrt(self.power/(4*math.pi*(math.pow(10,-11))))

    def findMaximumRadius(self):
        ty = (self.power + 110)/(10 * self.n)
        return math.pow(10,ty)



