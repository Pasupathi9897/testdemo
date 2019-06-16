#How to reverse a dictionary
n=int(input("enter the number of elemnents to be entered"))
dict={}
dict1={}
for i in range(0,n):
    first=input("key")
    second=input("values")
    dict[first]=second
print(dict)
print(dict.items())
for i,j in dict.items():
    dict1[j]=i
print(dict1)