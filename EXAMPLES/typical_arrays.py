#!/usr/bin/env python

fruits = ['apple', 'cherry', 'orange', 'kiwi', 'banana', 'pear', 'fig']
name = "Eric Idle"
knight = ('King', 'Arthur', 'Britain')
record = b'abc'

print(fruits[3])  # <1>
print(name[0])  # <2>
print(knight[1])  # <3>

a = "thing"

s1 = '100\u00B0'
print(s1)
b1 = s1.encode()
print(b1)
print(s1 == b1)





