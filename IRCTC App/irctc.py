import mysql.connector


conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="irctc_python"
)

cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS EmpData (
	uid INT(16) PRIMARY KEY AUTO_INCREMENT, 
	username VARCHAR(20) NOT NULL, 
	password VARCHAR(20) NOT NULL, 
	email VARCHAR(32)
	);""")

cursor.execute("""
	INSERT INTO EmpData(uid, username, password, email) VALUES(1, 'arceusomkar7', 'password_', 'xyz@mail.com')
	""")

cursor.execute("SELECT * FROM EmpData;")

data = cursor.fetchall()

for rows in data:
  print(rows)


class IrctcApp:

    def __init__(self, userName, passWord):
        self.userName = userName
        self.passWord = passWord

    def searchTrains(trains):
      pass

