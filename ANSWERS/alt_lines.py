#!/usr/bin/env python

alt_in = open("../DATA/alt.txt")
a_out = open("a.txt", "w")
b_out = open("b.txt", "w")

for line in alt_in:
    if line.startswith('a'):
        a_out.write(line)
    else:
        b_out.write(line)

alt_in.close()
a_out.close()
b_out.close()
