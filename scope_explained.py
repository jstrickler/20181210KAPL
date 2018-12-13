#!/usr/bin/env python

x = 100 # GLOBAL variable

def spam():
    y = 50  # LOCAL variable
    # x = 101 # LOCAL variable
    print("in spam(): x is", x)

# local -> non-local (nested) -> global
#   -> builtin

spam()
print("in main: x is", x)
# print("y is", y)

