# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
a=[int(x) for x in input().split()]
a.sort()
print(a[-1])
for i in range(0,len(a)):
 k=0
 for j in range(0,len(a)):
        if(a[i]==a[j]):
            k+=1
 if(k<=1):
     p=a[i]
     break
print(p)