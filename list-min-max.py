list=[1,2,3,4,13,44,33]
for i in range(0,len(list)):
    if(list[i]<list[i-1]):
        temp=list[i]
        list[i]=list[i-1]
        list[i-1]=temp
    max=list[i]
print(max)

for i in range(0,len(list)):
    if(list[i]>list[i-1]):
        temp=list[i]
        list[i]=list[i-1]
        list[i-1]=temp
    min=list[i]
print(min)
