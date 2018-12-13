#!/usr/bin/env python

# line by line
with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        print(raw_line, end='')
print('-' * 60)

# line by line
with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip('\n\r')
        print(line)
print('-' * 60)

# entire file
with open('DATA/mary.txt') as mary_in:
    contents = mary_in.read()
    print(repr(contents))
    print()
    new_contents = contents.replace('Mary', 'Marvin')
    print(new_contents)
print('-' * 60)

# list of lines with newlines
with open('DATA/mary.txt') as mary_in:
    lines = mary_in.readlines()
    print(lines)
print('-' * 60)

# list of lines without newlines
with open('DATA/mary.txt') as mary_in:
    contents = mary_in.read()
    lines = contents.splitlines()
    del contents
    print(lines)
print('-' * 60)

