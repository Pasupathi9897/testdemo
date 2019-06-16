import pymysql
db=pymysql.connect("localhost","root","admin","pp")
cursor=db.cursor()
str="create table user(id int,name varchar(10),email varchar(10),moblie int(10),login_id varchar(20),password varchar(20),date_of_birth date)"
#str="create table pasu2(id int,name varchar(20))"
cursor.execute(str)
db.close()
print("created table")