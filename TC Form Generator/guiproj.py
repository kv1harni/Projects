import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk, filedialog, simpledialog
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from datetime import date
import csv
import tcgenerator as stg

#initializing the tkinter Class
root = Tk()

#global SchoolName variable
sklName = "No. 1 Harni Road"

#initializing the StudentTcGenerator class
tcApp = stg.TcGeneratorApp(sklName=sklName)
    





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

#generating A Tc Form
def GenerateTcForm(reason):
    treeFocousData = tree.item(tree.focus())
    st_details = treeFocousData["values"]

    #calling a function from TcApp module
    student = tcApp.generateFormDetails(st_details)
    tcApp.GenerateTcFormImg(student=student, reason=reason)

    
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
 
    #========================================================================
    #Accessing Tree coloumns to show headings   
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

#search function ====================================================
def call_result(entry_value):  
    value1 = (entry_value.get())   
    print(value1)

def searchStudent():
    newPopup = Toplevel(frame)
    newPopup.title('Search for Student')

    logophoto = tk.PhotoImage(file = 'logo.png')
    newPopup.wm_iconphoto(False, logophoto)
    newPopup.geometry("500x500")

    entry_value = tk.StringVar()
    x = Entry(newPopup, textvariable=entry_value)
    x.place(relx = 0.2, rely=0.2)
    
    b1 = Button(newPopup, text = "search", command=call_result(entry_value))
    b1.place(relx=0.4, rely=0.4)

root.title("Transfer form Generator")
root.geometry("1100x550+200+200")

#icon==========================================
logophoto = tk.PhotoImage(file = 'logo.png')
root.wm_iconphoto(False, logophoto)

#frame =========================================
frame = Frame(root)
frame.pack(pady=25)



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

btn3 = Button(root, text="Search", width=60, height=2, font=30, fg = "white", bg="#0078d7", command=searchStudent)
btn3.pack(padx=10, pady=20)


root.mainloop()
