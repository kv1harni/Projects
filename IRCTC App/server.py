from colorama import Cursor
import pymysql
from telegram import Credentials

sqlCredentials = {
  "mySqlPassword": "pass",
  "sqlUserName": "userName",
  "database": "databaseName"
}

serverConnection = pymysql.connect(
  host="remotemysql.com",
  user=sqlCredentials["sqlUserName"],
  password=sqlCredentials["mySqlPassword"],
  db=sqlCredentials["database"]
)

myCursor = serverConnection.cursor()
