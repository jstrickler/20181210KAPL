#!/usr/bin/env python

list1 = list()

# x = list(ITERABLE)

things = ['a', 5, 4.234, None, True, '', ['stuff', 'nonsense']]


list2 = []

record = 'NY NJ MA CT RI'
fields = record.split()
print(fields, '\n')

cities = ['Albany', 'Poughkeepsie', 'White Plains',
        'Schenectady', 'Saratoga Springs', 'Kinderhook']

cities.append('Troy')
print(cities, '\n')
cities.insert(0, 'Newburgh')
print(cities, '\n')
cities.insert(3, 'East Egg')
print(cities, '\n')

more_cities = ['Hyde Park', 'West Point', 'Syracuse']

cities.extend(more_cities)

print(cities, '\n')

del cities[0]
print(cities, '\n')

del cities[2:6]  # delete items 2-5
print(cities, '\n')

x = cities.pop()
print(x)
print(cities, '\n')

x = cities.pop(3)
print(x)
print(cities, '\n')

cities.remove('West Point')
print(cities, '\n')

a = [1, 2, 3]
b = [4, 5, 6]

c = a + b
# a.extend(b)

a += b
print("a:", a, '\n')








