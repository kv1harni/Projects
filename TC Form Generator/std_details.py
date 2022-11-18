import csv
import pandas as pd

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
# GETTING DETAILS FROM CSV
# =========================================================================


def get_student_detail(adm_no = None):
    global adm_nos
    global data_dict
    rows = [row for row in data_dict]

    student_dict = None
    if check_student(adm_no) == True:
        for row in rows:
            if row['Admission Number'] == str(adm_no):
                student_dict = row
                break

        return student_dict
