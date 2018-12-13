#!/usr/bin/env python
import sys  # load module sys.py
# import re   # find and load module re.py

print(sys.argv)
if len(sys.argv) < 3:
    print("Syntax: command_line_params.py arg arg ...")
    exit()

#  LIST[INDEX] (0-based)
print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])

