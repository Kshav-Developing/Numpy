import numpy as npy

a = npy.array([[23, 21, 34, 12, 85]])

# Changing element of the array
a[0,1] = 45
a[0,4] = 55
a[0, 0] = 1

print(a)