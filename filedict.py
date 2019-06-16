dict={}
fo=open("keys.txt","r+")
f=open("value.txt","r+")
str=fo.read()
str1=f.read()
print(str)
a=str.split(" ")
print(a)
b=str1.split(" ")
for i in range(0,len(a)):
    dict[a[i]]=b[i]
print(dict)