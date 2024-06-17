import numpy as np

print('1D Array')
a = np.array([1, 2, 3, 4, 5])
print(a)
type(a)
#----------------------------
print('2D Array')
b = np.array([[1, 2, 3, 4, 5], 
              [6, 7, 8, 9, 10]])
print(b)
#----------------------------
print('3D Array')
c = np.array([[[1, 2, 3, 4, 5], 
              [6, 7, 8, 9, 10], 
              [11, 12, 13, 14, 15]]])
print(c)
#size = Tells about no. of elements in that array
print(a.size)
print(b.size)
#shape = (rows, cols)
print(a.shape)
#dtype = Type of Data Present in the array
print(b.dtype)
print(c.dtype)
#transpose of matrix
d = np.array([[1, 2, 3, 4.2, 5], 
              [6, 7, 8.9, 9, 10], 
              [11, 12, 13, 14, 15]])

d.transpose()

#np.empty((rows, cols), dtype)
np.empty((4,4), dtype = float)

#np.arange(start, end, step)
a = np.arange(1,20, 2)
print(a)

#arr.reshape((rows, cols))
a = a.reshape((3,3))

# a.ravel(): (i) Return only reference/view of original array 
# (ii) If you modify the array you would notice that the value of original array also changes. 
# (iii) Ravel is faster than flatten() as it does not occupy any memory.
# (iv) Ravel is a library-level function.

# a.flatten() : (i) Return copy of original array
# (ii) If you modify any value of this array value of original array is not affected. 
# (iii) Flatten() is comparatively slower than ravel() as it occupies memory.
# (iv) Flatten is a method of an ndarray object.
a = a.flatten()
a = a.ravel()
