import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk, filedialog 
import pandas as pd
import numpy 
# import studenTcGenerator as stg
root = Tk()

    
def readExcel(fileName):
    return ""

def GenerateTcForm():
    treeFocousData = tree.item(tree.focus())
    st_details = treeFocousData["values"]
    print(f"""
    =============K.V. No - 1 Harni Road vadodara===========
    ------------------Transfer Certificate-----------------\n\n
    Name of student : {st_details[1]}
    Adminssion Number : {st_details[0]}
    father\'s Name : {st_details[2]}
    Mother\'s Name : {st_details[3]}
    Class & Section : {st_details[4]} {st_details[5]}
    Session : {st_details[6]}
    """)

def OpenFile():
    filename = filedialog.askopenfilename(title="Open Student Details Excel File", filetypes=[("xlxs files", ".*xlsx"), ("All Files", "*.")])
    if filename: 
        try:
            filename = r"{}".format(filename)
            df = pd.read_excel(filename)

        except:
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
