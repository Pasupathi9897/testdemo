dict={}
j=0
n=int(input("enter the number of elements to be enter into directory"))
for i in range(0,n):
    first=int(input("enter the key"))
    second=input("enter the string")
    dict[first]=second
print(dict)
a=int(input("requried key"))
if(dict.__contains__(a)):
 print("key avalible")
 b=dict[a]
 print(b)
 for i in range(0,len(b)):
    if((b[i].__contains__('a'))|(b[i].__contains__('b'))|(b[i].__contains__('c'))):
     j=j+1
 print(j)
else:
    print("key not avalible")