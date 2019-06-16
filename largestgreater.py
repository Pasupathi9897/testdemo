list=[]
list1=[]
n=int(input("enter the no.of elements to enter"))
for i in range(0,n):
    list.append(int(input()))
print(list)
a=int(input("no.of greater elements needed"))
list.sort()
for i in range(n-a,n):
    list1.append(list[i])
print(list1)
