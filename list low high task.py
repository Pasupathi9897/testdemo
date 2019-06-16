list=[1,14,5,20,4,2,54,20,87,98,3,1,32]
lowval=14
highval=20
list1=[]
for i in range(0,len(list)):
 if(list[i]<lowval):
    list1.append(list[i])
for i in range(0,len(list)):
 if((list[i]>=lowval)&(list[i]<=highval)):
    list1.append(list[i])
for i in range(0,len(list)):
 if(list[i]>highval):
    list1.append(list[i])


print(list1)