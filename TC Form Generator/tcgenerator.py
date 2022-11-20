import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from datetime import date

#Generating a Class to use these functions as a module
#=====================================================================
class TcGeneratorApp(Exception):
    #==================================================================
    #Initializing The class with skl name for caching
    #=================================================================
    def __init__(self,sklName = None):
        self.sklName = sklName

    #Helper Function to check student
    def check_student(self,adm_nos = None, adm_no = None):
               
        #checking admission No. using if-else
        if adm_no in adm_nos:
            return True

        elif adm_no not in adm_nos:
            return False


    def generateFormDetails(self, st_details) -> dict:
        subs = []
        
        #Running a for loop To Append Subject List to A dict
        for i in range(9, 14):
            #if Sub is Not None Append it
            if i != "nan":
                subs.append(st_details[i])
            
            #if sub is None Continue the loop ignoring that Sub
            else:
                continue
        
        #creating a Dict that stores Data extracted from the 
        #Tkinter Tree  Object
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


    def GenerateTcFormImg(self,student, reason):


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
        for subject in student['subjects']:
            subs = subs + subject + ","
        subs = subs[:-1]

        # Subjects
        form_img_draw.text((650, 521), subs, fill =(0, 0, 0),font=ImageFont.truetype('Arial.ttf', 14))
        print(subs)   
        

        # Reason to leave
        form_img_draw.text((650, 465), reason,
                        fill =(0, 0, 0), font=ImageFont.truetype('Arial.ttf', 12))
        


        form_img.show()

        print(student)


    

