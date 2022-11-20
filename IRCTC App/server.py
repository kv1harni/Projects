import pymysql
from telegram import Credentials

sqlCredentials = {
  "mySqlPassword": "wVwYzJO5tv",
  "sqlUserName": "2BKSEWqFDK",
  "database": "2BKSEWqFDK"
}

serverConnection = pymysql.connect(
  host="remotemysql.com",
  user=sqlCredentials["sqlUserName"],
  password=sqlCredentials["mySqlPassword"],
  db=sqlCredentials["database"]
)

myCursor = serverConnection.cursor()
