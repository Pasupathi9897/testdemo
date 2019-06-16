#How do you find out the number of key-value dictionarypings present in a dictionary
dict={}
n=int(input("enter the n value"))
for i in range(0,n):
    first=input("enter the key")
    second=input("enter the value")
    dict[first]=second
print(dict)
print(len(dict))