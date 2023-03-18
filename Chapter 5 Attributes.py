import numpy as nm

a = nm.array([[3,4,5], [6,7,2], [32,53,10]])
print(a)

# Transposing the array (row to column and column to row [4x5 to 5x4])
print(a.transpose())

# Using iteration to print out all the elements 
for i in a.flat : 
    print(i)

# Printing out the dimension of the array (here it has 2 dimensions so the output would be 2)
print(a.ndim)

# Printing the number of elements in the array (the total number of elements are 9) 
print(a.size)

# Prints the total bytes consumed of array
print(a.nbytes)