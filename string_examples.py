#!/usr/bin/env python

cave_man = 'Barney Rubble'

print(str(cave_man))
print(repr(cave_man))

print(len(cave_man))

print(cave_man.upper())
print(cave_man.lower())
print(cave_man.count('B'))
print(cave_man.count('b'))
print(cave_man.lower().count('b'))

print(cave_man.replace(' ', '.'))

print(cave_man.index('Bar'))
print(cave_man.index('Rub'))
# print(cave_man.index('Foo'))  # raises error
# print(str.index(cave_man, 'Bar')) #weird

print(cave_man.replace('B', 'D').replace('b', 'd'))

print(cave_man.startswith('Foo'))
print(cave_man.startswith('Bar'))

print("Touch" in cave_man)
print("Rub" in cave_man)

# print(cave_man.contains('Rub'))  # not implemented

value = "12345"
print(value.isdigit())

s = '     All my exes live in Texas     '
print('|' + s.lstrip() + '|')
print('|' + s.rstrip() + '|')
print('|' + s.strip() + '|')
print()

s = 'xyxxxyyyxyxyxAll my exes live in Texasyxxxyyyyxyyxyyx'
print('|' + s.lstrip('xy') + '|')
print('|' + s.rstrip('xy') + '|')
print('|' + s.strip('xy') + '|')
print()

data = "123 445 993"
fields = data.split()
print(fields)

data = "123;455;32023"
fields = data.split(';')
print(fields)

data = "foo\rfar\nblah\rbaz"

lines = data.splitlines()
print(lines)

s = "spam"

print(len(s))
print(s.upper())



















