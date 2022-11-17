import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk, filedialog, simpledialog
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from datetime import date


# import studenTcGenerator as stg
root = Tk()

    
def readExcel(fileName):
    return ""

#Define a function to close the popup window
def close_win(top):
   top.destroy()

def insert_val(e):
   e.insert(0, "Hello World!")

#Define a function to open the Popup Dialogue

#creating pop up for field details
def popupwin():
   #Create a Toplevel window

   #Create an Entry Widget in the Toplevel window
   USER_INP = simpledialog.askstring(title="Test",
                                  prompt="What's your Reason? for tc\nErite in about 50 characters only:\n\n\n-----------------------------------------------------------------------", )

   GenerateTcForm(USER_INP)
#    #Create a Button to print something in the Entry widget
#    Button(top,text= "Insert", command= GenerateTcForm(USER_INP)).pack(pady= 5,side=TOP)
#    #Create a Button Widget in the Toplevel Window
#    button= Button(top, text="Ok", command=lambda:close_win(top))
#    button.pack(pady=5, side= TOP)






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
        if i != "nan":
            subs.append(st_details[i])
        else:
            continue

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


def GenerateTcForm(reason):
    student = formDetails()
    form_img = Image.open("formimg.jpg")
    form_img_draw = ImageDraw.Draw(form_img)
    myFont = ImageFont.truetype('Arial.ttf', 20)

    # Date of Application
    form_img_draw.text((650, 260), str(date.today()), fill =(0, 0, 0),font=myFont)

    # Student Name
    form_img_draw.text((650, 293), student['std_name'], fill =(0, 0, 0),font=myFont)
    
    # Class-Section (with year)
    form_img_draw.text((650, 327), f"{student['class']}-{student['section']}  ({student['session']})", fill =(0, 0, 0),font=myFont)
    
    # Father's Name 33diff
    form_img_draw.text((650, 360), student['f_name'], fill =(0, 0, 0),font=myFont)

    # Mother's name 
    form_img_draw.text((650, 393), student['m_name'], fill =(0, 0, 0),font=myFont)

    # Local Address
    form_img_draw.text((650, 433), student['local_address'], fill =(0, 0, 0),font=ImageFont.truetype('Arial.ttf', 12))

    subs = ""
    for i in student['subjects']:
        subs = subs + i + ","
    subs = subs[:-1]
    # Subjects
    form_img_draw.text((650, 521), subs, fill =(0, 0, 0),font=ImageFont.truetype('Arial.ttf', 14))
    print(subs)   
    

    # Reason to leave
    form_img_draw.text((650, 465), reason,
                     fill =(0, 0, 0), font=ImageFont.truetype('Arial.ttf', 12))
    


    form_img.show()

    print(student)
    
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
    btn2 = Button(root, text="Generate Tc", width=30, height=2, font=20,
                  fg = "white", bg="#0078d7", command=popupwin)
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
