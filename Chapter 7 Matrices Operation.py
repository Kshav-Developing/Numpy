import numpy as nm 

a = nm.array([[1,3,6], [1,8,0]])
b = nm.array([[2,3,4], [1,2,2]])

# Adding two arrays by using the rule of matrix
c = a + b       

# Multiplies two arrays (adjacently)
c = a * b

# Square root of an array 
c = nm.sqrt(a)

# Sums up all the elements of an array
c = a.sum()
print(c)

# Gives max and min value of an array
c, d = b.max(), b.min()
print(c)
print(d)

# returns the array number where one number is greater than other , e.g. => 5
e = nm.where(a>4)
print(e)

# gives the total number of non zero elements present in an array
f = nm.count_nonzero(a)
print(f)