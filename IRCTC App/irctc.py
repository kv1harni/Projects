import mysql.connector


conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="admin"
)

cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXSIST EmpData (username VARCHAR(20), password VARCHAR(20), email VARCHAR(32))")


class IrctcApp:

    def __init__(self, userName, passWord):
        self.userName = userName
        self.passWord = passWord

    def searchTrains(trains):
      pass
