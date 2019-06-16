import pymysql
f=open("t.txt","r")
a=f.readlines()
b=a[0].split(",")
db=pymysql.connect("localhost","root","admin","pp")
cursor=db.cursor()
#for i in range(0,len(b)):
str="insert into file (A,B,C,D) values (b[0+1],b[1+i],b[2+i],b[3+i])"
 #if(i==len(b)):
  #   break;
cursor.execute(str)
db.commit()
db.close()
print("data entered succesfully")