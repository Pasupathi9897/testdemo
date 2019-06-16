l=[0,0,7,4,2,1,3,5,6,7,8,9,1]
a=3
for i in range(0,len(l)):
 sum=0
 if(a<=len(l)):
        for i in range(a-3,a):
            sum=sum+l[i]
        if(sum==7):
            print("true")
        else:
            print("false")
        a=a+1



