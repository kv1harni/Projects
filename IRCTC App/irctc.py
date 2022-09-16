
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="admin"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE EmpData (username VARCHAR(255), password VARCHAR(255), email VARCHAR(255))")


class IrctcApp:

    def __init__(self, userName, passWord):
        self.userName = userName
        self.passWord = passWord

    def searchTrains(trains):
      pass