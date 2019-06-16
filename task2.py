list=[35,49,63,22,10,11,7,55]
print("enter the element to be searched")
a=10
for i in range(0,len(list)):
    if (list[i]==a):
        print("the was found")
        print(i)
for i in range(0,i):
    if(list[i]>list[i-1]):
     temp=list[i]
     list[i]=list[i-1]
     list[i-1]=temp
     min=list[i]
print("the min value of list 1 is")
print(min)
for i in range(i+1,len(list)):
    if(list[i]<list[i-1]):
        temp=list[i]
        list[i]=list[i-1]
        list[i-1]=temp
    max=list[i]
print(max)
sum=min+max
avg=sum/2
print(avg)