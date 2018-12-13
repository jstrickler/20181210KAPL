#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0:", f0, '\n')

f1 = [f.upper() for f in fruits]
print("f1:", f1, '\n')

# NEW_LIST = [EXPRESSION for VAR ... in ITERABLE if COND ...

squares = [i ** 2 for i in range(21)]
print('squares:', squares, '\n')

f2 = [f.upper() for f in fruits if f.startswith('p')]
print('f2:', f2, '\n')

f3 = [f for f in fruits if f.startswith('p')]
print('f3:', f3, '\n')

food = ['spam', 'spam', 'toast', 'spam', 'spam', 'spam', 'spam',
        'doughnuts', 'spam', 'spam', 'spam', 'eggs', 'spam', 'spam', ]

despammed = [f for f in food if f != 'spam']
print('despammed:', despammed, '\n')

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

last_names = [p[1] for p in people]
print('last_names', last_names, '\n')


r = range(100)
e = enumerate(fruits)
rv = reversed(fruits)
z = zip(['a', 'b', 'c'], [1, 2, 3])

print(r, e, rv, z)






