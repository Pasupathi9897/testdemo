list=[12,10,5,6,52,36]
k=2
n=len(list)
for i in range(0,k):
    a=list[i]
    list.append(a)

for i in range(0,k):
    list.remove(list[i])



print(list)
