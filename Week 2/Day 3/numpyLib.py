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

'''------numpy with string---'''
s1 = 'Akshit is my name'
s2 = 'I am an Indian'
np.char.add(s1, s2)
np.char.upper(s1)
np.char.lower(s1)
np.char.split(s1)
np.char.replace(s1, 'name', 'sirname')
print(np.char.center('good bye', 80, '*'))

'''----random with numpy----'''
np.random.random(1)
np.random.random((2,2))
np.random.randint(1,10)
np.random.randint(1,10, (3,4,5))
np.random.rand(2,2)
np.random.randn(2,2)
a = np.arange(1,10)
print(a)
np.random.choice(a)

'''------mathematics----'''
a = np.arange(0,18).reshape((6,3))
b = np.arange(20, 38).reshape((6,3))
print(a)
print(b)
np.add(a,b)
np.subtract(a,b)
np.multiply(a,b)
a.dot(b)
np.sum(b, axis = 1)
np.mean(b)
np.std(b)
np.log(b)
np.sqrt(b)

# save and load numpy array
n=np.array([10,20,30,40])
np.save("numpy_array",n)
np.load("numpy_array.npy")

'''----'''
n1=np.array([1,2,3,4 ])
n2=np.array([5,6,7,8])
print(np.vstack((n1,n2)))
print(np.hstack((n1,n2)))
print(np.column_stack((n1,n2)))

# #intersection and difference
ans=np.intersect1d(n1,n2)
print(ans)
print(np.setdiff1d(n1,n2) )
print(np.setdiff1d(n2,n1))
