list1=[1,2,3]
list2=[4,5,6]
ad=[]
add=0
if(len(list1)==len(list2)):
    for i in range(0,len(list1)):
     add=list1[i]
     ad.clear()
     for j in range(0,len(list2)):
        a=add+list2[j]
        print(a)
        ad.append(a)
     print(ad)
else:
    print("not existing")
