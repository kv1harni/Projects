import mysql.connector
import json
import traceback
import pymysql
from server import myCursor as cursor
from server import serverConnection as sConnection


#defining A class so that all these functions can be used later in GUI
class Admin:
    
    #defined A user Regestration Functions That would Register The Admin Person
    def adminSingUp(self, username, password, email, fullname):
        try:
            cursor.execute("insert into admin(emp_name, emp_username, emp_password, emp_mail) value(%s,%s, %s, %s)", 
                        (username, password, email, fullname))
            
            sConnection.commit()
            return "User Registered successfully"
        except Exception:
            traceback.print_exc()
        
