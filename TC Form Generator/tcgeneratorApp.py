import pandas as pd

class TcGeneratorApp:

    def __init__(self,sklName = None):
        self.sklName = sklName

    #Helper Functions
    def check_student(self,adm_nos = None, adm_no = None):
               
        #checking admission No. using if-else
        if adm_no in adm_nos:
            return True

        elif adm_no not in adm_nos:
            return False


    
        

