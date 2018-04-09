'''
learning how to use numpy
'''


import numpy as np

data = [[5.5,6,7],[1,5,8],[10,0,5],[12,12,7]]

print 'Row 1 is:', data[0]

x = np.array(data)

print 'Row 1 in numpy is:', x[0]
print 'Type Row 1, Col 1. Python', data[0][0], 'Numpy', x[0,0]

print 'First two rows:', x[0:2]
print 'First two cols:', x[:,0:2]

print 'First two rows and two cols:', x[:2,:2]

print 'Odd rows:', x[::2]
print 'Even rows:', x[1::2]

print 'Sum of all the elements:', x.sum()
print 'Maximum element:', x.max()
print 'Mean:', x.mean()
print 'Standard Deviation:', x.std()
print 'Median:', np.median(x)

print 'Sum of each row:', x.sum(axis=1)
print 'Sum of each col:', x.sum(axis=0)

print'Min of each row:', x.min(axis=1)
min_x = x.min(axis=1)
print 'Max of the min of each row:', min_x.max()
print 'Max of the min of each row:', x.min(axis=1).max()

print 'Rows 1 and 4:', x[[0,3]]

mask = [True, False, False, True]
print 'Rows 1 and 4:', x[mask]

print 'Is the entry greater than 5?', x > 5
print 'All of the values greater than 5:', x[x>5]

print 'All values in the fourth row greater than 10:', x[3][x[3]>10]

print 'Sum all values in the fourth row greater than 10:', x[3][x[3]>10].sum()

x[0,1]=10
x[1,1]= np.nan #nan = "not a number"

print 'Our new x:', x
print 'Maximum with a nan in it:', x.max() #=nan
print 'Minimum with a nan in it:', x.min() #=nan

#fortunately we can filter out nans

print 'Maximum using nanmax', np.nanmax(x)

#we can replace nans with 0 if we want

x[np.isnan(x)] = 0

print 'Our filtered x:', x

#print 'Our matrix shape:', x.shape() <-- shape is a field not a method, see below
print 'Our matrix shape:', x.shape

print 'Iterate over all the rows:'
for row in x:
	print 'row:', row

print 'Transpose of matrix:', x.T

print 'Iterate over all the cols:'
for row in x.T:
	print 'col:', row

print 'Saving to file'
np.save('mymatrix', x) #<--- binary file
np.savetxt('textmatrix.txt', x) #<--- text file

y_1 = np.load('mymatrix.npy')
y_2 = np.loadtxt('textmatrix.txt')
print y_1
print y_2

print 'Random value:', np.random.random() #U[0,1]
print 'Random gaussian:', np.random.normal() #N(0,1)
print 'Random N(10,9):', np.random.normal(10,3) #N(10, 3^2)
print  'Random beta:', np.random.beta(1,1) #beta(1,1)

print '3x4 matrix of gaussians:', np.random.normal(size=(3,4))
print 'Vector of gaussians with increaing means:', np.random.normal([1,5,100])

def foo(a,b,c=1):
	print a,b,c

foo(0,5) #uses c's default value
foo(0,5,5) #uses c=5
foo(0,5,c=7)#uses x=7

z = np.arange(9)
print 'z =', z
z = z.reshape((3,3))
print 'Reshaped z:', z


#BROADCASTING
 #lets you apply a thing that isn't the same shape across all matching things

d = np.array([3,7,2], dtype=float)
print 'd:', d

print 'First three rows of x time z (element wise):', x[:3] * z

print 'First three rows of x times z (matrix multiply):', x[:3].dot(z)

print 'Multiply every element of d by its corresponding row in z:', z * d[:,np.newaxis] #z: (3x3) d: 3 ---> d: (3x1)


















