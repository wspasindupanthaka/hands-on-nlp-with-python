import numpy as np

#generate arrays with upper limit, in here 10
np.arange(10)

#generate arrays in range
np.arange(1,10)

#specify the steps, in here 2
np.arange(1,10,2)

#specify the datatype
np.arange(1,10,dtype='float64')

arr = np.arange(1,10)

#specify the dimension
arr.ndim

#
arr.size

arr.dtype

arr.itemsize

#memory usage
arr.itemsize * arr.size

#Numpy is mainly used for vectorized calculations
#That means it is fast when compared to normal python operations

#normal python, have to execute 10^6 loops
%timeit list1 = range(1,1000000)

#numpy, have to execute 10^5 loops
%timeit list1 = np.arange(1,1000000)

#1000000*547ns/1000=547000µs microseconds used to create list from normal python
#100000*3.06µs=306000µs microseconds used to create list from numpy

#convert any python array to numpy array
np.asarray([1,2,3,4,5])

list2d = [[1,2,3],[4,5,6]]
arr2d = np.asarray(list2d)

#create array of zeros of given dimension of given type
arrzeros = np.zeros((3,4),dtype='int32')

#generate any amount of numbers in a given range
np.linspace(1,4,num=4)
np.linspace(1,4,num=8)
np.linspace(1,4,num=8,endpoint=False)

#generate array of random numbers between 0 and 1 in given dimension
rarr=np.random.random((3,4))

#column-wise max value
np.max(rarr,axis=0)

#row-wise max value
np.max(rarr,axis=1)


np.min(rarr,axis=0)
np.min(rarr,axis=1)


np.median(rarr,axis=0)
np.median(rarr,axis=1)


new_rarr=np.reshape(rarr,(12,))
new_rarr=np.reshape(rarr,(12,1))

rarr = np.random.random((4,5))
