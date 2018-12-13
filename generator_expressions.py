#!/usr/bin/env python


data = [1.2342342, 3.39203983, 2.239042934, 8.2930294203,
        10.29304293402934, 5.23940239402394]


d1 = [round(f, 2) for f in data]
print(d1, '\n')

#    (EXPR for VAR ... in ITERABLE if COND ...)
d2 = (round(f, 2) for f in data)
print(d2, '\n')

for f in d2:  # loop over rounded version of elements in data
    print(f)
print('Done.\n')

for f in d2:  # loop over rounded version of elements in data
    print(f)
print('Done.\n')

