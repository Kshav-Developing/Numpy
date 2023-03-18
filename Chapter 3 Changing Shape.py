import numpy as np 

a = np.arange(0, 50)

# Changing the shape of the array (row x column)
b = a.reshape(2, 25)    # row x column = no. of elements, otherwise it will give an error
b = b.ravel()

print(b)
print(b.shape)