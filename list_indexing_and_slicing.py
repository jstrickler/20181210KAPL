#!/usr/bin/env python

cities = ['Albany', 'Poughkeepsie', 'White Plains',
        'Schenectady', 'Saratoga Springs', 'Kinderhook']

cities.append('Troy')
cities.insert(0, 'Newburgh')
cities.insert(3, 'East Egg')

more_cities = ['Hyde Park', 'West Point', 'Syracuse']
cities.extend(more_cities)

print(cities, '\n')
print(cities[0], '\n')
print(cities[4], '\n')
print(cities[len(cities) - 1], '\n')
print(cities[-1], cities[-2], '\n')
print(cities, '\n')

a = cities[0:4]   # items 0-3
print(a, '\n')

# S[START:STOP]  S[:STOP]  S[START:]  S[START:STOP:STEP]
print(cities[:4])
print(cities[3:8], '\n')
del cities[2:4]

print(cities, '\n')
del cities[-3:]  # delete last 3
print(cities, '\n')

cities[4:6] = ['Buffalo'] * 2

print(cities, '\n')

pos = cities.index('Buffalo')
print(pos)
print(cities.index('Buffalo', pos + 1))
print()

# print(cities.index('Elk'))
# target = 'Buffalo'
# pos = 0
# while True:
#     pos = cities.index(target, pos)
#     print(pos)
#     pos += 1
#     if pos >= len(cities):
#         break

x = ['a', 'b', 'c']
print(x * 3)
print(x + x)


actor = 'Brad Pitt'

print(actor[:4], actor[5:8], actor[-3:])



