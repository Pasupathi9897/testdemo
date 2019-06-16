dict={}
n=int(input("enter the number of values"))
for i in range(0,n):
 first = input("enter the key for insertion")
 second = input("enter the value for insertion")
 dict[first] = second
print(dict)
n1=int(input("enter the no.of elements to be removed"))
for i in range(0,n1):
 e=str(input("enter the key"))
 if(dict.__contains__(e)):
    del dict[e]
 else:
    print("we cant remove the key")
print(dict)
