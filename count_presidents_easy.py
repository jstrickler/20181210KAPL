#!/usr/bin/env python
from collections import Counter

with open('DATA/presidents.txt') as potus_in:
    states = [line.split(':')[6] for line in potus_in]
    c = Counter(states)

print(c)
print(c['New York'])

print(c.most_common(3))

