list=[3,1,2,4,5,9,13,14,12]
list1=[]
list2=[]
for i in range(0,len(list)):
    if(i%2==0):
        list1.append(list[i])
    else:
        list2.append(list[i])
for i in range(1,len(list1)):
    if(list1[i-1]>list1[i]):
        temp=list1[i-1]
        list1[i-1]=list1[i]
        list1[i]=temp
for i in range(1,len(list2)):
    if(list2[i-1]<list2[i]):
        temp=list2[i-1]
        list2[i-1]=list2[i]
        list2[i]=temp
list.clear()
for i in range(1,len(list1)):
    list.append(list1[i])
for i in range(1, len(list2)):
    list.append(list2[i])
print(list)