import pymysql
db=pymysql.connect("localhost","root","admin","pp")
cursor=db.cursor()
str="create table file(A int,B varchar(10),C varchar(10),D varchar(10))"
cursor.execute(str)
db.close()
print("successfull")