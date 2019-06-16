#how to replace the key from value and value from key in dictionary
dict={}
n=int(input("enter the n value"))
for i in range(0,n):
    first=input("enter the key")
    second=input("enter the value")
    dict[first]=second
print(dict)
for i in range(0,n):
    temp=dict[first]
    dict[first]=second
    second=temp
print(dict)

