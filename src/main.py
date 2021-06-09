import mysql.connector
from database.mysql_connector import MySQLConnector

database = MySQLConnector(host="127.0.0.1",user="root",password="my_clave_secreta",database="modelado")


result = database.executeQuery("select * from user")

for row in result:
    print (row)