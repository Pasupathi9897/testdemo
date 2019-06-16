#p=a/d
#d=((1+i)^n-1)/i*(1+i)^n
#i=rate/12
amount=float(input("enter the loan"))
rate=int(input("enter the interest percentage"))
rate1=int(input("enter the final interset percentage"))
inc=float(input("enter the increment percentage"))
year=int(input("enter the no.of years"))
r=[]
t=rate
n=year*12
for i in range(0,n):
    if(rate<rate1):
       rate=t+(inc*i)
       r.append(rate)
for i in range(0,len(r)):
 ia=(r[i]/100)/12
 p=1
 for j in range(0,n):#d=((pow((ia+1),n))-1)/ia*(pow((ia+1),n))
    p=p*(1+ia)
 d=float((p-1)/(ia*p))
# print(d)
 q=float(amount/d)
 total=float(q*n)
 print("when the interest is",(r[i]))
 print("interst is",r[i],"%""mounthly payment",float(q),"total payment",float(total))