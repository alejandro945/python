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