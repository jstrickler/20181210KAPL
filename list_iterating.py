#!/usr/bin/env python

cities = ['Albany', 'Poughkeepsie', 'White Plains',
        'Schenectady', 'Saratoga Springs', 'Kinderhook']

cities.append('Troy')
cities.insert(0, 'Newburgh')
cities.insert(3, 'East Egg')

more_cities = ['Hyde Park', 'West Point', 'Syracuse']
cities.extend(more_cities)

print(cities, '\n')


# for VAR ... in ITERABLE
for wombat in cities:
    # city = cities[0]
    # city = cities[1]
    # ...
    if len(wombat) > 8:
        print(wombat.upper())
print()

actor = 'Brad Pitt'
for letter in actor:
    print(letter)
print()


for i, city in enumerate(cities):
    print(i, city.upper())
print()
print(list(enumerate(cities)), '\n')

for i, city in enumerate(cities, 1):
    print(i, city.upper())
print()
