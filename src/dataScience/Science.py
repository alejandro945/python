import numpy as np
from numpy.core.fromnumeric import reshape
# np array ro list is faster because take less spaces than a normal python list
a = np.array([(1,2,3),(4,5,6)])
#Finding the dimension of an array
print(a.ndim)
# Calculating the byte size
print(a.itemsize)
# Reshape is when you change the number of [rows and columns] which gives a new view to an object.
b = a.reshape(6,1)
print(b)
# Slicing
print(a[1,2])
#Looking for numbers in both rows? Here colon represents all the rows, including zero
print(a[0:,1])
#Linspace for print n numbers between a range; For example the follw expression will print 15 number in 10-30 range.
c = np.linspace(10,30,15)
print(c)
# Sum an array in a blink
print(a.sum())
# Min and Max values
print(c.max()) # => 30 -- Obviusly
print(c.min()) # => 10 -- Obviusly
# Data structures
# Merge sort in-place, O(n log2 n)
# Quicksort, O(n log n)