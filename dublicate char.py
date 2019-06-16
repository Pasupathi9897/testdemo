str="this is the best the beast"
for i in range(0,len(str)):
    a=str[i]
    print(a)
    s=0
    for j in range(1,len(str)):
     if(a==str[j]):
        print(str.find(str[j]))
