#!/usr/bin/env python
from pprint import pprint

knight_data = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight_data[name] = {
            'title': title,
            'color': color,
            'quest': quest,
            'comment': comment,
        }

pprint(knight_data)
print()

print(knight_data['Lancelot'])
print(knight_data['Lancelot']['color'])
print()

# for  key, value   in dictionary items: ...
for name, data in knight_data.items():
    print(f"{data['title']} {name} seeks ... {data['quest']}")










