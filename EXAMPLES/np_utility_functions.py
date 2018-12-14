#!/usr/bin/env python
import numpy as np

a = np.array(
    [[70, 31, 21, 76, 19, 5, 54, 66],
     [23, 29, 71, 12, 27, 74, 65, 73],
     [11, 84, 7, 10, 31, 50, 11, 98],
     [25, 13, 43, 1, 31, 52, 41, 90],
     [75, 37, 11, 62, 35, 76, 38, 4]]
)  # <1>

print(a, '\n')

r1 = np.where(a > 50)
print(r1, '\n')

i1 = np.isin(a, 50)
print(i1, '\n')

i2 = (a == 50)
print(i2, '\n')
