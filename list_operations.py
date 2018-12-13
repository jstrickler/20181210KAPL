#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

print(len(fruits), min(fruits), max(fruits))
print(sorted(fruits))
print()

for fruit in reversed(fruits):
    print(fruit.upper())
print()


first_names = ['Vincent', 'Boris', 'Bela']
last_names = ['Price', 'Karloff', 'Lugosi']

horror_actors = zip(first_names, last_names)
print(list(horror_actors), '\n')  # GENERATOR!!

horror_actors = list(zip(first_names, last_names))

print(horror_actors, '\n')


for i, fruit in enumerate(fruits):
    print(i, fruit.lower())
print()

if 'ORANGE' in fruits:
    print('ORANGE!')

flags = [True] * 10
print(flags)

junk = ['a', 'b', 'c']
print(junk * 10, '\n')

for i in range(10):
    print("Whoo-hoooo!")
print()

# range(STOP)  range(START, STOP)  range(START, STOP, STEP)

for i in range(5, 101, 5):
    print(i, end=' ')
print('\n')











