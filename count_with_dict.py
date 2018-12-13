#!/usr/bin/env python


counts = {}

with open('DATA/breakfast.txt') as breakfast_in:
    for raw_line in breakfast_in:
        item = raw_line.rstrip()
        if item in counts:
            counts[item] = counts[item] + 1
            #  counts[item] += 1
        else:
            counts[item] = 1

        # counts[item] = counts.get(item, 0) + 1

for food, count in sorted(counts.items()):
    print(food, count)

print(counts)

