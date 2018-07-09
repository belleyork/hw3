from random import randint


class Bus:
    def __init__(self, name, busNum, destination):
        self.name = name
        self.busNum = busNum
        self.destination = destination

        destinationChoice1 = 0
        full = 0

        num = [1, 2, 3, 4, 5, 6, 7]
        des = ['a', 'b', 'c', 'd', 'e', 'f']

        for i in range(len(des)):
            destinationChoice = des[i]

            full = randint(1, 5)

            if destination == destinationChoice and full != 5:
                print(name + ' can ride the bus to ' + destination +
                      ' because there are only ' + str(full) + ' people on it.')
            elif destination == destinationChoice and full == 5:
                print(name + ' cannot ride the bus to ' + destination +
                      ' because the bus is full with 5 people.')
