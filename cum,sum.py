list=[]
list1=[]
sum=0
n=int(input("enter the n value"))
for i in range (0,n):
    a=int(input())
    list.append(a)
print(list)
for i in range(0,n):
    sum=sum+list[i]
    list1.append(sum)
print(list1)
