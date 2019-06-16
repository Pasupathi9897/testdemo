list=[]
list1=[]
list2=[]
n=int(input("enter the no.of elements to enter"))
for i in range(0,n):
    list.append(int(input()))
print(list)
for i in range(0,n):
    if(list[i]%2==0):
        list1.append(list[i])
    else:
        list2.append(list[i])
print("even list",list1)
print("odd list",list2)

