import pandas as pd
import csv
import os
import time

# import mysql.connector

# conn = mysql.connector.connect(host="localhost",
# user="root",
# password="1234",
# database="student")

# =========================================================================
# PROCESSING EXCEL DATA
# =========================================================================
# Loading data
excel_data = pd.read_excel('studentList.xlsx')
print("LOADED EXCEL DATA")

# Converting to CSV
csv_data = excel_data.to_csv('temp_csv.csv', index=None)
print("CONVERTED TO CSV")

# Creating dataframe
df = pd.read_csv('temp_csv.csv')
print("DATAFRAME CREATED")


# =========================================================================
# DEFINING REQUIRED VALUES
# =========================================================================

csv_file = open('temp_csv.csv')
data_dict = csv.DictReader(csv_file)
adm_nos = [x for x in df['Admission Number']]


# =========================================================================
def check_student(adm_no):
    # adm_no = int(input("Enter Admission Number of student: "))
    global adm_nos

    if adm_no in adm_nos:
        return True

    elif adm_no not in adm_nos:
        return False


# ========================================================================
# CHECK DETAILS FUNCTION
# ========================================================================
def student_detail():
    global adm_nos
    global data_dict
    rows = [row for row in data_dict]

    student_dict = None
    print("CHECK STUDENT ENTRY\n")
    adm_no = int(input("Enter student's admission number: "))
    if check_student(adm_no) == True:
        for row in rows:
            if row['Admission Number'] == str(adm_no) + ".0":
                student_dict = row
                break

        print(
            f"Name: {student_dict['Student Name']}\nClass: {student_dict['Class']}-{student_dict['Section']}\nAddress: {student_dict['Local Address']}"
        )

    elif check_student(adm_no) == False:
        print(f"Student with admission number {adm_no} does not exist")


# =========================================================================
# DELETE FUNCTION
# =========================================================================
def del_student():
    print("DELETE STUDENT ENTRY\n")

    adm_no = int(input("Enter student's admission number: "))

    if check_student(adm_no) == True:
        print(df)
        df.drop(df.index[(df['Admission Number'] == adm_no)],
                axis=0,
                inplace=True)
        print("Entry deleted")
        print(df)

    elif check_student(adm_no) == False:
        print(f"Student with admission number {adm_no} does not exist already")


# =========================================================================
# DEFINING MAIN MENU
# =========================================================================
def main_menu():
    print("WELCOME TO TC FORM GENERATOR!\n")
    print("What function do you want to use?\n")
    print(
        "1. Generate TC from (not completed)\n2. Check student entry\n3. Delete student entry\n4. Exit"
    )

    user_choice = int(input("Enter you choice: "))

    os.system("clear")

    if user_choice == 1:
        print("Sorry, but this feature is not yet completed")

    elif user_choice == 2:
        student_detail()

    elif user_choice == 3:
        del_student()

    elif user_choice == 4:
        print("Bye!...")
        time.sleep(2)
        exit()


main_menu()
