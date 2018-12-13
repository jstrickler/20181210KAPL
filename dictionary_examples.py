#!/usr/bin/env python

d1 = dict()

d2 =  {'red': 5, 'purple': 3, 'white': 5, 'orange': 99}

d25 = {('red', 'blue'): 8, ('orange', 'green'): 19}

d26 = {'red': [5, 6], 'purple': [10, 3, 4], 'white': 'wombat', 'orange': 99}

combos = [('Schenectady', 'NY'), ('Durham', 'NC'), ('Boston', 'MA')]
cities = dict(combos)
print(cities)

print(d1)
print(d2)


cities['Las Vegas'] = 'NV'

print(cities)
cities['Troy'] = 'NY'
state = cities.setdefault('Troy', 'MI')
print(state)
state = cities.get('Boston')
print(state)

state = cities.get('Raleigh', 'NOT FOUND')
print(state)

# cities['Troy'] = 'MI'

print(cities)

more_cities = {'New Bern': 'NC', 'Newburgh': 'NY', 'Boston': 'PA'}

cities.update(more_cities)

print(cities)

print('Durham' in cities)
print('Wombatville' in cities)


print(cities['Troy'])

print(cities.items(), '\n')

for city, state in cities.items():
    print(city, state)
print()


for city, state in sorted(cities.items()):
    print(city, state)
print()














