str="this is the best the beast"
a=str.split(" ")
for i in range(0,len(a)):
    b=a[i]
    for j in range(i+1,len(a)):
        if(b==a[j]):
         a.pop(a[j])

print()