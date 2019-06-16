'''def a(n):
    return n+n
num=[1,2,3,4,5]
r=map(a,num)
print(list(r))
'''

'''''
def l(a,b):
    return a+b
num=['apple','ball','cat']
n=['sujana','tinava','ra']
r1=map(l,num,n)
print(list(r1))
'''''
'''''
num=[1,2,3,4,5]
num1=[5,4,3,2,1]
r=map(lambda x,y:x+y,num,num1)
print(list(r))
'''''
l = ['sat', 'bat', 'cat', 'mat']
re=map(list,l)
print(list(re))