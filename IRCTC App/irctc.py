import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234"
)

print(mydb)

class IrctcApp:

    def __init__(self, userName, passWord):
        self.userName = userName
        self.passWord = passWord

    def loginAdmin(self, userName, passWord):
        pass