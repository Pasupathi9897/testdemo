num=121
p=0
while(num>0):
   p=p*10+p%10
   num=num//10
if(p==num):
    print("it is palintrome")
else:
    print("not palintrome")