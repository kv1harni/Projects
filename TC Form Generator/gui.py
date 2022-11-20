from tkinter import *
from tkinter import ttk, filedialog
import pandas as pd
from tcgenerator import TcGeneratorApp

root = Tk()
root.geometry("1080x600")


#===============frame 2===============================
sheet_frame = Frame(bd = 4, relief=RIDGE)

#creating A Tree View
sheet_tree = ttk.Treeview(sheet_frame)

#placing the tree
sheet_frame.place(relx=0.35, y=0, relheight=0.97, relwidth=0.62)


#========================================================
# #adding scroll bars---------
# sheet_scrolly = Scrollbar(sheet_frame)
# sheet_scrollx = Scrollbar(sheet_frame, orient=HORIZONTAL)

# sheet_scrollx.pack(side=BOTTOM, fill=X)
# sheet_scrolly.pack(side=RIGHT, fill=Y)

# #packing the scroll bar ------------------------------
# sheet_tree.pack()

# #internal configs for scrollbars
# sheet_scrolly.config(command=sheet_tree.yview)
# sheet_scrollx.config(command=sheet_tree.xview)

# sheet_tree.config(yscrollcommand=sheet_scrolly.set)
# sheet_tree.config(xscrollcommand=sheet_scrollx.set)
# sheet_tree.config(selectmode=BROWSE)

#Global FIle open/closed variable--------------
fileStatus = False

#A global Reason Button
reason_button = None


def file_open():
    global fileStatus
    filename = filedialog.askopenfile(
        initialdir="./",
        title="Select students data sheet",
        filetypes=(('Excel File', '*.xlsx'), ('CSV File', '*.csv'), ("All Files", "*.*"))
    )


    print(str(filename))
    if filename:
        try:
            df = pd.read_excel(filename.name)

            
        except Exception as e:
            print(e)

        # Clearing tree view if already any
        clear_tree()

        # Setting up new treeview
        sheet_tree["column"] = list(df.columns)
        sheet_tree["show"] = "headings"
        
        # Iterating through column list
        for col in sheet_tree["column"]:
            sheet_tree.heading(col, text=col)
        
        # Putting data in treeview
        df_rows = df.to_numpy().tolist()
        for row in df_rows:
            sheet_tree.insert("", "end", values=row)
        
        #adding scroll bars---------
        if fileStatus == False:
            sheet_scrolly = Scrollbar(sheet_frame)
            sheet_scrollx = Scrollbar(sheet_frame, orient=HORIZONTAL)

            sheet_scrollx.pack(side=BOTTOM, fill=X)
            sheet_scrolly.pack(side=RIGHT, fill=Y)

            #packing the scroll bar ------------------------------
            sheet_tree.pack()

            #internal configs for scrollbars
            sheet_scrolly.config(command=sheet_tree.yview)
            sheet_scrollx.config(command=sheet_tree.xview)

            sheet_tree.config(yscrollcommand=sheet_scrolly.set)
            sheet_tree.config(xscrollcommand=sheet_scrollx.set)
            sheet_tree.config(selectmode=BROWSE)

        
            gen_button.config(state=ACTIVE)

        else:
            pass
        
        sheet_tree.place(x=0, y=0, relheight=1, relwidth=1)
    fileStatus = True

def clear_tree():
    sheet_tree.delete(*sheet_tree.get_children())

def get_selected():
    row = sheet_tree.item(sheet_tree.focus())
    print(row)


#==================frame1=============================================
# SETTING THE BUTTONS IN THE MENU THING
menu_frame = Frame()
menu_frame.place(relx=0, rely=0, relheight=1, relwidth=0.30)

sheet_button = Button(menu_frame, text="Open File", width=30, height=2, font=20, fg = "white", bg="#0078d7", command=file_open)
sheet_button.place(x=0, y=0)

#
gen_button = Button(menu_frame, text="Generate Tc", width=30, height=2, font=20, fg = "white", bg="#0078d7", command=get_selected, state=DISABLED)
gen_button.place(x=0, y=60)

search_heading = Label(menu_frame, text="Search Student details:\n(Enter admission number)", font=12)
search_heading.place(x=0, y=280)
search_entry = Entry(menu_frame)
search_entry.place(x=185, y=282, relwidth=1)
search_button = Button(menu_frame, text="Search", width=10, height=1, font=10, fg = "white", bg="#0078d7")
search_button.place(relx=0.35, y=320)


root.mainloop()
