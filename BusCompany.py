class Towns:
    def __init__(self, town1='none', town2='none'):
        self.town1 = town1
        self.town2 = town2


class Buses:
    def busCount(self, busNum=0):
        self.busNum = busNum
        return busNum

    def bus1(self, seating=4):
        self.seating = seating

        return seating

    def bus2(self, seating=5):
        self.seating = seating

        return seating

    def bus3(self, seating=10):
        self.seating = seating

        return seating

    def bus4(self, seating=9):
        self.seating = seating

        return seating

    def bus5(self, seating=11):
        self.seating = seating

        return seating

    def bus6(self, seating=2):
        self.seating = seating

        return seating


class Person:
    def __init__(self, name):
        self.name = name


class Roads:
    def __init__(self, road='none'):
        self.road = road

    def roads(self): return self.road
