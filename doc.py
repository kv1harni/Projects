import pickle

def insertRec():
    doctor_id = int(input('Enter doctor id:'))
    doctor_name = input('Enter Name:')
    hospital_id = int(input('Enter hosptial id:'))
    joining_date=input("Enter date:")
    speciality=input("Enter speciality:")
    salary=float(input("Enter Salary:"))

    rec = [doctor_id,doctor_name,hospital_id,joining_date,speciality,salary]

    f = open('hospital.dat','ab')
    pickle.dump(rec,f)
    f.close()


def readRec():
    f = open('hospital.dat','rb')
    while True:
        try:
            rec = pickle.load(f)
            print(rec)
        except EOFError:
            break
    f.close()


def updaterec():
    f = open('hospital.dat','rb')
    r1 = []
    while True:
        try:
            r = pickle.load(f)
            r1.append(r)
        except EOFError:
            break
    f.close()
    d_id=int(input("Enter doctor id to update:"))
    if d_id in r1:
        doctor_name = input('Enter new Name:')
        hospital_id = int(input('Enter new hosptial id:'))
        joining_date=input("Enter new date:")
        speciality=input("Enter new speciality:")
        salary=float(input("Enter new Salary:"))
        for i in range (len(r1)):
            if r1[i][0]==d_id:
                r1[i][1] = doctor_name
                r1[i][2]=hospital_id
                r1[i][3]=joining_date
                r1[i][4]=speciality
                r1[i][5]=salary
        f = open('hospital.dat','wb')
        for x in r1:
            pickle.dump(x,f)
        f.close()
    else:
        print("Record not found...")

def menu():
    while True:
        print('''
    1. Write a record to the file
    2. Read all the records to the file
    3. Update Record
    4. Exit
    ''')
        ch = int(input('Enter you choice:'))
        if ch == 1:
            insertRec()
        elif ch == 2:
            readRec()
        elif ch == 3:
            updaterec()
        elif ch == 4:
            print("Thank you, visit again!")
            break
menu()