import pymysql
db=pymysql.connect("localhost","root","admin","pp")
cursor=db.cursor()
str="insert into pasu (id,name) values (1,'pasu')"
cursor.execute(str)
db.commit()
db.close()
print("data entered succesfully")