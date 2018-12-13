#!/usr/bin/env python

person = 'Bill', 'Gates', 'Microsoft'

print(person[0], person[1])
print(person[:2])

first_name, last_name, product = person  # ITERABLE UNPACKING!

print(first_name, last_name)

people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple', 'NeXT'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey','Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux', 'Git'),
]

print(people[0])
print(people[0][0])
print(people[0][0][0])
print()

for first_name, last_name, *product in people:
    print(first_name, last_name, product)
print()

values = ['a', 'b', 'c', 'd', 'e', 'f']

x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)
print()

actors = [
    ('Brad', 'Pitt'),
    ('Angelina', 'Jolie'),
    ('Matt', 'Damon'),
    ('George', 'Clooney'),
]

for first, last in actors:
    print(first, last)
print()











