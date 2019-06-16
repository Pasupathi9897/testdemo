#How do you check whether a particular key/value exist in a dictionary
dict={}
n=int(input("enter the n value"))
for i in range(0,n):
    first=input("enter the key")
    second=input("enter the value")
    dict[first]=second
print(dict)
e=input("enter the key")
f=input("enter the values")
if((dict.__contains__(e))|(dict.__contains__(f))):
    print("the element was present in the dictionary")
else:
        print("dont found")