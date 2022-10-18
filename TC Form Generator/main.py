import pandas as pd

class FormGen:
    def __init__(self, data_location:str):
        print("INITIALIZED")
        self.excel_data = pd.read_csv(data_location)
        self.adm_nos = [x for x in self.excel_data['Admission Number']]


    def check_student(self):
        adm_no = int(input("Enter Admission Number of student: "))

        if adm_no in self.adm_nos:
            print("Student enrolled")
            return True
        elif adm_no not in self.adm_nos:
            print("Student not enrolled")
            return False

app = FormGen(data_location = "student data.csv")

app.check_student()
