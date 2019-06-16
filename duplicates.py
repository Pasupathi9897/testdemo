list=[10,20,30,20,20,30,40,50,-20,60,60,-20,-20]
list1=[]
print(list)
for i in range(0,len(list)):
    for j in range(i+1,len(list)):
      if(list[i]==list[j]):
         list1.append(list[i])
print(list1)
a=set(list1)
print(a)
