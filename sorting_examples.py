#!/usr/bin/env python
from operator import itemgetter

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

n1 = sorted(nums)
print("n1:", n1, '\n')

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = sorted(fruits)
print("f0:", f0, '\n')

fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f1 = sorted(fruits)
print("f1:", f1, '\n')

f2 = sorted(fruits, key=str.lower)
print("f2:", f2, '\n')

def clean(s):
    return s.lower().strip()

f3 = sorted(fruits, key=lambda s: s.lower().strip())
print('f3:', f3, '\n')

# fruits.sort(key=clean)

n2 = sorted(nums, key=str)
print("n2:", n2, '\n')

f3 = sorted(fruits, key=len)
print("f3:", f3, '\n')

def custom1(f):
    return len(f), f.lower()

f4 = sorted(fruits, key=custom1)
print("f4:", f4, '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey','Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux'),
]

for first_name, last_name, _ in sorted(people):
    print(first_name, last_name)
print('-' * 60)

def by_last_name(p):
    return p[1], p[0]

for first_name, last_name, _ in sorted(people, key=by_last_name):
    print(first_name, last_name)
print('-' * 60)

for first_name, last_name, _ in sorted(people, key=lambda p: (p[1], p[0])):
    print(first_name, last_name)
print('-' * 60)

#  lambda P ... : RETURN-VALUE
from operator import itemgetter

for first_name, last_name, _ in sorted(people, key=itemgetter(1,0), reverse=True):
    print(first_name, last_name)
print('-' * 60)
