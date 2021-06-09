from database.connector import Connector
import mysql.connector

class MySQLConnector(Connector):
    def __init__(self, host, user, password, database) -> None:
        super().__init__(host, user, password, database)
        self.mydb = self.connect()

    def connect(self) -> bool:
        mydb = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database)
        
        return mydb

    def executeSentence(self, sql,values):
        mycursor = self.mydb.cursor()
        mycursor.execute(sql,values)
        self.mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    
    def executeQuery(self, sql):
        mycursor = self.mydb.cursor()
        mycursor.execute(sql)
        return mycursor.fetchall()
        