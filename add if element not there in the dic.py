#How to add the key if and only if it is not present inside the dictionary
dict={}
n=int(input("enter the number of values"))
for i in range(0,n):
 first = input("enter the key for insertion")
 second = input("enter the value for insertion")
 dict[first] = second
print(dict)
n1=int(input("enter the no.of elements to be added"))
for i in range(0,n1):
 e=input("enter the key")
 if(dict.__contains__(e)):
        print("we cant enter the key")
 else:
        second=input("enter the value for insertion")
        dict[e]=second
print(dict)

