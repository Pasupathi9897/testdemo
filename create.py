import pymysql
db=pymysql.connect("localhost","root","admin","pp")
cursor=db.cursor()
str="create table pasu1(id int,name varchar(20))"
cursor.execute(str)
db.close()
print("Table created succesfully in database")