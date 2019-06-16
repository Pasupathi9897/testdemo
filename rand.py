import pymysql
db=pymysql.connect("localhost","root","admin","pp")
cursor=db.cursor()
for i in range(0,10000):
 str="insert into user (id,name,email,moblie,login_in,password,date_of_birth) values (%d,str(i),str(i),str(i),str(i),str(i),i)"
 cursor.execute(str)
 db.commit()
db.close()
print("data entered succesfully")