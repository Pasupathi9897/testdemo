n=lambda x:x+10
print(n(2))
l=lambda a,b:a+b
print(l(10,20))
def myfun(n):
    return lambda x:x*n
a1=myfun(2)
print(a1(2))