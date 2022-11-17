import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk, filedialog 
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from datetime import date


# import studenTcGenerator as stg
root = Tk()

    
def readExcel(fileName):
    return ""

def check_student(adm_no):
    # adm_no = int(input("Enter Admission Number of student: "))
    global adm_nos

    if adm_no in adm_nos:
        return True

    elif adm_no not in adm_nos:
        return False

def formDetails() -> dict:
    subs = []
    treeFocousData = tree.item(tree.focus())
    st_details = treeFocousData["values"]

    for i in range(9, 14):
        subs.append(st_details[i])

    st_details_dict = {
            "adm_no" : st_details[0],
            "std_name" : st_details[1],
            "f_name" : st_details[2],
            "m_name" : st_details[3],
            "class" : int(st_details[4][:-2]),
            "section" : st_details[5],
            "session" : st_details[6],
            "local_address" : st_details[7],
            "subjects" : subs
    }
    return st_details_dict


def GenerateTcForm():
    student = formDetails()
    form_img = Image.open("formimg.jpg")
    form_img_draw = ImageDraw.Draw(form_img)
    myFont = ImageFont.truetype('Arial.ttf', 20)

    # Date of Application
    form_img_draw.text((650, 257), str(date.today()), fill =(0, 0, 0),font=myFont)

    # Student Name
    form_img_draw.text((650, 290), student['std_name'], fill =(0, 0, 0),font=myFont)
    
    # Class-Section (with year)
    form_img_draw.text((650, 324), f"{student['class']}-{student['section']}  ({student['session']})", fill =(0, 0, 0),font=myFont)
    
    # Father's Name 33diff
    form_img_draw.text((650, 357), student['f_name'], fill =(0, 0, 0),font=myFont)

    # Mother's name 
    form_img_draw.text((650, 390), student['m_name'], fill =(0, 0, 0),font=myFont)

    # Local Address
    form_img_draw.text((650, 430), student['local_address'], fill =(0, 0, 0),font=ImageFont.truetype('Arial.ttf', 12))

    # Reason to leave
    # ----------------------

    subs = ""
    for i in student['subjects']:
        subs = subs + i + ","
    subs = subs[:-1]
    # Subjects
    form_img_draw.text((650, 521), subs, fill =(0, 0, 0),font=ImageFont.truetype('Arial.ttf', 14))
    print(subs)
    

    form_img.show()

    print(student)
    print(f"""
    =============K.V. No - 1 Harni Road vadodara===========
    ------------------Transfer Certificate-----------------\n\n
    Name of student : {student['std_name']}
    Adminssion Number : {student['adm_no']}
    father\'s Name : {student['f_name']}
    Mother\'s Name : {student['m_name']}
    Class & Section : {student['class']} {student['section']}
    Session : {student['session']}
    """)

def OpenFile():
    filename = filedialog.askopenfilename(title="Open Student Details Excel File", filetypes=[("xlxs files", ".*xlsx"), ("All Files", "*.")])
    if filename: 
        try:
            filename = r"{}".format(filename)
            df = pd.read_excel(filename)

        except Exception as e:
            print(e)
            messagebox.showerror("Error", "You can\'t access this file type")

        

    tree.delete(*tree.get_children())
    
    # treeScroll = Scrollbar(frame)
    # treeScroll2 = Scrollbar(frame, orient="horizontal")

    # treeScroll.pack(side=RIGHT, fill=Y)
    # treeScroll2.pack(side=BOTTOM, fill='x')
    # tree.pack()

    # treeScroll.config(command=tree.yview)
    # treeScroll2.config(command=tree.xview)
    # tree.config(yscrollcommand= treeScroll.set)
    # tree.config(xscrollcommand= treeScroll2.set)

    

    
    tree['column'] = list(df.columns)
    tree['show'] = "headings"

    #defining heading title

    for col in tree["column"]:
        tree.heading(col, text=col)
    
    #getting the data through numpy
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        tree.insert("", "end", values=row)

    #button
    btn2 = Button(root, text="Generate Tc", width=30, height=2, font=20, fg = "white", bg="#0078d7", command=GenerateTcForm)
    btn2.pack(padx=10, pady=20)




root.title("Transfer form Generator")
root.geometry("1100x550+200+200")

#icon==========================================
logophoto = tk.PhotoImage(file = 'logo.png')
root.wm_iconphoto(False, logophoto)

#frame =========================================
frame = Frame(root)
frame.pack(pady=25)

#treeView

tree = ttk.Treeview(frame)
treeScroll = Scrollbar(frame)
treeScroll2 = Scrollbar(frame, orient="horizontal")

treeScroll.pack(side=RIGHT, fill=Y)
treeScroll2.pack(side=BOTTOM, fill='x')
tree.pack()

treeScroll.config(command=tree.yview)
treeScroll2.config(command=tree.xview)
tree.config(yscrollcommand= treeScroll.set)
tree.config(xscrollcommand= treeScroll2.set)

#button
btn = Button(root, text="Open", width=60, height=2, font=30, fg = "white", bg="#0078d7", command=OpenFile)
btn.pack(padx=10, pady=20)



root.mainloop()
