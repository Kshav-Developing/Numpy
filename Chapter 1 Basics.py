import numpy as np

# An array is like an organized list of python. It is an efficient way of using data
# an array must be entered like this [[row], [column]]
ar = np.array([[3, 34, 24, 13]], np.int8)     # "np.int8" is used to convert the storage of integers into 8 bits, which means it won't be accepting big numbers

print(ar)
print(ar[0,1])      # array[row, column] will print the integer situated in the row and column entered
print(ar[0])        # entering only row will give the whole integers of that row
print(ar[0,0])      
print(ar.shape)     # prints out the "row x column" of the array
print(ar.size)      # prints the total size of the array
print(ar.atype)     # prints the data type of the integers (int8, int64)  