import numpy as np 

# Axis is a complicated thing, axis number starts from 0
# Axis is dimension in which an array is made (1D, 2D, 3D, 4D etc)
# For example, 2D has two axes - x and y
# 2D axis = (Axis 0, Axis 1), 1D axis = (Axis 0)
# Axis 0 = row and Axis 1 = column

a = [[1,2,3],[4,5,6],[7,8,9]]
c = np.array(a)

# axis 0 will add all the values in the row1, row2 and row3
# here it will work as r1 = 1+4+7 = 12, r2 = 2+5+8 = 15, r3 = 3+6+9 = 18
print(c.sum(axis=0))

# here it will work as c1 = 1+2+3 = 6, c2 = 4+5+6 = 15, c3 = 7+8+9 = 24
print(c.sum(axis=1))
