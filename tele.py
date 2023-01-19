import csv
def add_record():
  f=open("telephone.csv",'a',newline='')
  wo=csv.writer(f)
  s_id=int(input("Enter Subscriber ID:"))
  name=input("Enter name of subscriber:")
  brand=input("Enter brand of telephone:")
  typ=input("Enter customer type:")
  price=float(input("Enter Price:"))
  wo.writerow([s_id,name,brand,typ,price])
  print("Record addedd Successfully.")
  f.close()

def display_record():
  f=open("telephone.csv",'r')
  ro=csv.reader(f)
  l=list(ro)
  for i in range(1,len(l)):
    print(l[i])
  f.close()

def search_record():
  f=open("telephone.csv","r")
  ro=csv.reader(f)
  sid=input("Enter id to search:")
  found=0
  for i in ro:
    if sid==i[0]:
      found=1
      print("Record Found:")
      print(i)
  if found==0:
    print("Record not found...")
  f.close()
def menu():
  while True:
    print('''
    1. Add record
    2. Display record
    3. Search record
    4. Exit
    ''')
    ch=int(input("Enter your choice:"))
    if ch==1:
      add_record()
    elif ch==2:
      display_record()
    elif ch==3:
      search_record()
    elif ch==4:
      print("Thank you, See you again!!")
      break
    else:
      print("Invalid Choice")
menu()