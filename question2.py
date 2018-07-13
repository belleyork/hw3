from BusCompany import Buses
from BusCompany import Person
from BusCompany import Towns
from BusCompany import Roads

destination1 = ['Apple Vill', 'Blue Ville', 'Cranberry',
                'Dog Town', 'EveryoneVill', 'FriendsVille']
destination2 = ['Georgia', 'Houston', 'Ithica',
                'Joseph', 'Kentucky', 'Loserville']
roads = ['Bella RD', 'Jam DR', 'Short RD', 'Tall Ave', 'Schumacaer Ave']
busPeople = []
bus = Buses().busCount()
person = Person('Raquel')
person1 = Person('Bella')
content = ''
people = 0

busPeople.append(person1.name)
for i in range(len(destination1)):
    a = Towns(destination1[i], destination2[i])
    bus += 1

    newBus = 'Buses().' + 'bus' + str(bus) + '()'
    newBus = eval(newBus)

    busPeople.append(person.name)

    if len(busPeople) > newBus:
        content = ' is full'
    else:
        content = ' has a seat'

    for num in range(10):  # this will make a bunch of chairs and put them into a list
        number = num * num
        # picks a person from the population
        people = number % len(busPeople)

    for p in range(len(busPeople)):
        if people > len(roads) - 1:
            people = int(people / 9)

    print('bus_' + str(bus) + ' is going to town ' +
          a.town1 + ' and town ' + a.town2 + content + ' and it is traveling on ' + roads[int(people)] + '.')
