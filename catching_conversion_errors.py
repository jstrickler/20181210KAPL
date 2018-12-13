#!/usr/bin/env python


x = "123.45.9302"

try:
    f = float(x)
except ValueError as err:
    print(err)
else:
    print(f)

def foo(x):
    if isinstance(x, (float, int)):
        return x ** 2
    else:
        raise TypeError("arg must be numeric")


for value in 1, 2, "abc", 3:
    try:
        print(foo(value))
    except TypeError as err:
        print(err)

