#!/usr/bin/env python

john_countries = """Canada
Mexico
Barbados
China
China
China
China
UK
UK
UK
UK
UK
Austria
Spain
Bulgaria
Israel""".splitlines()

clare_countries = """Denmark
UK
Spain
Kenya
Mexico
Barbados
Norway
Sweden
Canada""".splitlines()



print()

john = set(john_countries)
clare = set(clare_countries)
# john.add('France')
# for i in range(1000000):
#     john.add('France')
print(john)
print(clare)
print()


print("Both:", john & clare, '\n')
print("Either:", john | clare, '\n')
print("Just one:", john ^ clare, '\n')
print("Just Clare:", clare - john, '\n')
print("Just John:", john - clare, '\n')



with open('DATA/breakfast.txt') as breakfast_in:
    contents = breakfast_in.read()
    items = contents.splitlines()
    print("all items:", items, '\n')
    unique_items = set(items)
    print('unique items:', unique_items)
