list=[10,121,133,155,141,252]
list1=[]
for i in range(0,len(list)):
 num=list[i]
 a=0
 while num>0:
    a=a*10+num%10
    num=num//10
 if(a==list[i]):
  list1.append(list[i])
print(list1)
print(len(list1))