from BusCompany import Buses
from BusCompany import Person
from BusCompany import Towns
from BusCompany import Roads

# list of destinations for the buses to go to
destination1 = ['Apple Vill', 'Blue Ville', 'Cranberry',
                'Dog Town', 'EveryoneVill', 'FriendsVille']
destination2 = ['Georgia', 'Houston', 'Ithica',
                'Joseph', 'Kentucky', 'Loserville']

# list of roads for the buses to travel on
roads = ['Bella RD', 'Jam DR', 'Short RD', 'Tall Ave', 'Schumacaer Ave']
busPeople = []

bus = Buses().busCount()  # calls the function busCount in class Buses
person = Person('Raquel')
person1 = Person('Bellca')
content = ''
people = 0

busPeople.append(person1.name)  # appends person1 into the list busPeople

for i in range(len(destination1)):
    a = Towns(destination1[i], destination2[i])
    bus += 1

    newBus = 'Buses().' + 'bus' + str(bus) + '()'
    newBus = eval(newBus)  # turns string into

    if len(busPeople) > newBus:  # if the amount of people that want to go on the bus is greating tjan the seating of bus then it is full
        content = ' is full'
    else:  # otherwise it is not
        content = ' has a seat'

    for num in range(10):  # this will make a bunch of chairs and put them into a list
        number = num * num
        # picks a person from the population
        people = number % len(busPeople)
        busPeople.append(person.name)

    # no matter how large the list of busPeople, people will always be in range of roads
    for p in range(len(busPeople)):
        if people > len(roads) - 1:
            people = int(people / 9)

    print('bus_' + str(bus) + ' is going to town ' +
          a.town1 + ' and town ' + a.town2 + content + ' and it is traveling on ' + roads[int(people)] + '.')
