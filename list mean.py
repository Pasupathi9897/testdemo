num=123456
list=[]
while(num>0):
 a=num%10
 num=num//10
 list.append(a)

print(list)

min=list[0]
max=list[0]
for i in range(0,len(list)):
    if(list[i]<min):
        min=list[i]
print(min)
for i in range(0,len(list)):
    if(list[i]>max):
        max=list[i]
print(max)
mean=(min+max)/2
print("mean of min and max is")
print(mean)

