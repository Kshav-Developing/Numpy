import numpy as np 

a = np.array([[1,2,3,4,5,6,7,8,23,21,234,11,54]])
b = np.array([11])

# Gives the index of biggest value element
print(a.argmax())

# Gives the index of smallest value element
print(a.argmin())

# Gives the index of sorted elements
print(a.argsort())

# These attributes can be used in other dimensional arrays too (2D, 3D) but it will automatically arrange the dimesion to 1D and will print the index according to it

# Gives maximum value according to the axis mentioned
print(a.argmax(axis=0))


