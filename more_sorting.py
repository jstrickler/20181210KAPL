#!/usr/bin/env python

fruits = ['Cherry', 'apple', 'banana', 'Peach', 'date', 'pear']

print(sorted(fruits), '\n')

def nothing(item):
    retval = len(item), item.lower()
    print("ITEM:", item, "RETVAL:", retval)
    return retval

print(sorted(fruits, key=nothing), '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple'),
    ('Larry', 'Wall', 'Perl'),
    ('Larry', 'Ellison', 'Oracle'),
]

print(sorted(people), '\n')

def junk(person):
    retval = person[1], person[0]
    print("PERSON:", person, "RETVAL:", retval)
    return retval

print(sorted(people, key=junk), '\n')


