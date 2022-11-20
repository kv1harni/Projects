from tkinter import *

class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("K.V. No - 1 Student Record Management System")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text="Student Management System",bd = 10, font=("Impact", 25, "bold"))
        title.pack(side=TOP, fill=X)

        # mnage students - clm 1
        manage_frame = Frame(self.root, bd = 4, relief=RIDGE)
        manage_frame.place(x = 35, y = 70, width=450 , height = 560)
        
        m_title = Label(manage_frame,text="Details...", font=("Impact", 15, "bold"))
        m_title.grid(row=0, columnspan=2, pady=15)



        #students details - clm 2
        detail_frame = Frame(self.root, bd = 4, relief=RIDGE)
        detail_frame.place(x = 500, y = 70, width=800 , height = 560)


root = Tk()
ob = Student(root)
root.mainloop()