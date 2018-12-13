#!/usr/bin/env python

potus_counts = {}

with open('DATA/presidents.txt') as potus_in:
    for line in potus_in:
        fields = line.split(":")
        state = fields[6]
        if state in potus_counts:
            potus_counts[state] += 1
        else:
            potus_counts[state] = 1

# print(potus_counts)

def by_value(item):
    return item[1], item[0]

for state, count in sorted(potus_counts.items(), key=by_value):
    print(state, count)
print('-' * 60)

# s1 = sorted(sorted(potus_counts.items(), key=???), key=???)

s2 = sorted(s1)
for state, count in s2:
    print(state, count)


