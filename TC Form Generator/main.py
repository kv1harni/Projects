import pandas as pd


excel_data = pd.read_csv("student data.csv")
adm_nos = [x for x in excel_data['Admission Number']]


def check_student():
    adm_no = int(input("Enter Admission Number of student: "))

    if adm_no in adm_nos:
        print("Student enrolled")
        return True
    elif adm_no not in adm_nos:
        print("Student not enrolled")
        return False

check_student()
