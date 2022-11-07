import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk, filedialog 
import pandas as pd


root = Tk()

    
def readExcel(fileName):
    return ""
def OpenFile():
    filename = filedialog.askopenfile(title="Open Student Details Excel File", filetypes=[("Excel files", "*.xlsx; *.xls")])
    
    if filename: 
        try:
            filename = r"{}".format(filename)
            df = pd.read_excel(filename)

        except:
            messagebox.showerror("Error", "You can\'t access this file type")

    tree.delete()

    tree['column'] = list(df.columns)
    tree['show'] = "headings"



root.title("Transfer form Generator")
root.geometry("1100x400+200+200")

#icon==========================================
logophoto = tk.PhotoImage(file = 'logo.png')
root.wm_iconphoto(False, logophoto)

#frame =========================================
frame = Frame(root)
frame.pack(pady=25)

#treeView

tree = ttk.Treeview(frame)
tree.pack()


#button
btn = Button(root, text="Open", width=60, height=2, font=30, fg = "white", bg="#0078d7", command=OpenFile)
btn.pack(padx=10, pady=20)



root.mainloop()
