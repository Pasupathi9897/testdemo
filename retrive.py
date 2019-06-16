#How do you retrieve a value associated with a given key from the dictionary
dict={}
n=int(input("enter the n value"))
for i in range(0,n):
    first=input("enter the key")
    second=input("enter the value")
    dict[first]=second
print(dict)
a=input("enter the needed element")
for i in range(0,n):
    if(dict.__contains__(a)):
       print(dict(a))
