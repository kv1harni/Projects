import pickle
while True:
  print('''
        1. Add Record
        2. Display Record
        3. Search Record
        4. Exit
  ''')
  ch=int(input("Enter your choice:"))
  l=[]
  if ch==1:
    f=open("shoes.dat","ab")
    s_id=int(input("Enter Shoes ID:"))
    name=input("Enter shoes name:")
    brand=input("Enter Brand:")
    typ=input("Enter Type:")
    price=float(input("Enter Price:"))
    l=[s_id,name,brand,typ,price]
    pickle.dump(l,f)
    print("Record Added Successfully.")
    f.close()
  elif ch==2:
    f=open("shoes.dat","rb")
    while True:
      try:
        dt=pickle.load(f)
        print(dt)
      except EOFError:
        break
    f.close()
  elif ch==3:
    si=int(input("Enter shoes ID:"))
    f=open("shoes.dat","rb")
    fl=False
    while True:
      try:
        dt=pickle.load(f)
        for i in dt:
          if i==si:
            fl=True
            print("Record Found...")
            print("ID:",dt[0])
            print("Name:",dt[1])
            print("Brand:",dt[2])
            print("Type:",dt[3])
            print("Price:",dt[4])
      except EOFError:
        break
    if fl==False:
      print("Record not found...")
    f.close()
  elif ch==4:
    break
  else:
    print("Invalid Choice")