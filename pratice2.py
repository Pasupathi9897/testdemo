import numpy as np
#In this lecture we will discuss how to select elements or groups of elements from an array
arr=np.arange(0,11)
print(arr)
#The simplest way to pick one or some elements of an array looks very similar to python lists
print(arr[8])
print(arr[0:2])
#Numpy arrays differ from a normal Python list because of their ability to broadcast
arr[0:5]=100
print(arr)