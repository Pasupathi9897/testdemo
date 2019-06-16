import numpy as np
my_list=[1,2,3]
print(my_list)
print(np.array(my_list))
my_matric=[[1,2,3],[4,5,6],[7,8,9]]
print(my_matric)
print(np.array(my_matric))
#arrange:Return evenly spaced values within a given interval
print(np.arange(0,10))
print(np.arange(0,11,3))
#Generate arrays of zeros or ones
print(np.zeros(3))
print(np.zeros((5,5)))
print(np.ones(3))
print(np.eye(4))#diadonal elements
#random
#Numpy also has lots of ways to create random number arrays:
#rand
#Create an array of the given shape and populate it with random samples from a uniform distribution over [0, 1].
print(np.random.rand(3))
print(np.random.rand(5,5))
#rand:Return a sample (or samples) from the "standard normal" distribution. Unlike rand which is uniform
print(np.random.randn(3))
print(np.random.randn(5,5))
#randint:Return random integers from low (inclusive) to high (exclusive)
print(np.random.randint(4,10))
print(np.random.randint(1,100,10))
#array attributes and methos:Let's discuss some useful attributes and methods or an array
aar=np.arange(25)
aar1=np.random.randint(0,50,10)
print(aar)
print(aar1)
#reshape:Returns an array containing the same data with a new shape
print(aar.reshape(5,5))
#max,min,argmin,argmax:These are useful methods for finding max or min values. Or to find their index locations using argmin or argmax
print(aar.max())
print(aar.min())
print(aar.argmin())
print(aar.argmax())
#shape:Shape is an attribute that arrays have (not a method)
a=np.arange(10)
print(a.shape)
print(a.reshape(1,10))
print(a.reshape(1,10).shape)
print(a.reshape(10,1))
#dtype:You can also grab the data type of the object in the array
print(a.dtype)
