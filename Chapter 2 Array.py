import numpy as nm

# There are five ways by which we can create an array

listarray = nm.array([[1,2,3], [5,4,3], [78,54,23]])    # The normal way of creating array using the python list
dictarray = nm.array({34, 23})                          # This creates an array of "object" type which is not suggested to use for data analysis
zeros = nm.zeros((2,5))                                 # creates an array of zeroes with the size 2x5
rangearray = nm.arange(1,20)                            # creates an array with the range provided
linspace = nm.linspace(1,20,10)                         # creates an array of equal linear spacing ".linspace(range1, range2, no.of elements)"
emp = nm.empty((4,6))                                   # gives empty array with random elements
emplike = nm.empty_like(listarray)                      # creates an array of same size as mentioned in the funtion ".empty_like(array)"
ident = nm.identity(10)                                 # creates an array of identity matrix (having elements only 0 and 1) of the size given in the arguments

print(ident)



