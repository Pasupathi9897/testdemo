list=[5,4,3,6,7,2,1]
a=[1,2,3,48,6442,45,6,78]
for i in range(0,len(list)):
    for j in range(i+1,len(list)):
      if(list[i]<list[j]):
        temp=list[i]
        list[i]=list[j]
        list[j]=temp

print(list)
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
      if(a[i]>a[j]):
        temp=a[i]
        a[i]=a[j]
        a[j]=temp

print(a)


