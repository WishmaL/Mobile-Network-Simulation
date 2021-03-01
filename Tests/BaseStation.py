
from Tests.Main import users


class BaseStation:
    "This is a Base Station class"

    baseStation1 = (0, 5000)
    baseStation2 = (10000, 0)
    baseStation3 = (10000, 10000)

    def __init__(self, name, xValue, yValue):

        self.name = name
        self.xValue = xValue
        self.yValue = yValue

    print(users)

