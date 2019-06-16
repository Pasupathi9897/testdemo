list=[0,1,0,1,0,1,0,1,1,1,1,0,0,0,1,0,1,0,0,0]
list1=[]
for i in range(0,len(list)):
    if(list[i]==0):
        list1.append(list[i])
for i in range(0, len(list)):
    if(list[i]==1):
     list1.append(list[i])
print(list1)
