of=open("C:\\Users\\DELL\\Desktop\\first.txt","r+")
test=of.readlines()
t=test.split(" ")
print(t)
max=-1
for i in range(0,len(t)):
    if(max<len(t[i])):
        max=len(t[i])
        mm=t[i]
print(mm)