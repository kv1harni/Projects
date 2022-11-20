import re
import mysql.connector
import json
import traceback
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
            print("User Registered successfully")
        except Exception:
            traceback.print_exc()
        

    def adminLogIn(self, username, password):
        try:
            exec = cursor.execute('SELECT * FROM admin WHERE emp_username=%s AND emp_password=%s', (username, password))
            empId, empName, empUsername, empPassword, empMail = cursor.fetchone()

            return f"Welcome {empName},\nYour emp Id is {empId}"
        except Exception:
            traceback.print_exc()

        