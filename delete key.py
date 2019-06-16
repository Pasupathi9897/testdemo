#How to delete a key from a dictionary
dict={}
n=int(input("enter the value of n"))
for i in range(0,n):
    first = input("enter the value of key to be insected")
    second = input("enter the value of value to be insected")
    dict[first]=second
print(dict)
d=input("enter the element to be deleted in directory")
del dict[d]
print(dict)