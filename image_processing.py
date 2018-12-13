#!/usr/bin/env python
import numpy as np
from scipy.ndimage.filters import gaussian_filter
import matplotlib.pyplot as plt

a = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
])


print(a)
print(a[0])
print(a[-1])
print(a[0,0])  # matlab-like
print(a[0][0]) # python-like
print(a[0,0:2])
# data = np.loadtxt("some_data.csv")
# # create numpy array
#
# result = gaussian_filter(data)
#
# plt.plot(result)
# plt.show()
#
