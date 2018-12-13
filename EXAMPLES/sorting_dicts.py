#!/usr/bin/env python

colors = dict(red=5, green=18, blue=1, pink=0, grey=27, yellow=5)

print(colors)
print(colors.items())

# sort by key
for color, num in sorted(colors.items()):  # <1>
    print(color, num)

print()

# sort by value
for color, num in sorted(colors.items(), key=lambda e: (e[1], e[0])): # <2>
    print(color, num)
