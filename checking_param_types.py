#!/usr/bin/env python


def add_integers(x, y):
    if not (isinstance(x, int) and isinstance(y, int)):
        raise TypeError("args must be ints")

    return x + y
