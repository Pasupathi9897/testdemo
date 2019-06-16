#How do you add given key-value pair to dictionary if and only if it is not present in the dictionary?
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
 f=input("enter the value")
 if((dict.__contains__(e))&(dict.__contains__(f))):
        print("we cant enter the key")
 else:
        dict[e]=f
print(dict)
