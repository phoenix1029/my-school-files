import pandas as pd
import matplotlib.pyplot as pl

file_path =r"C:\Users\STUDENT LOGIN\Desktop\project\studentdata.csv"
#1
def data_csv():
    n = input("Enter the number of students:\t")
    while not n.isdigit() or int(n) <= 0:
        print("Invalid number of students.")
        n = input("Enter the number of students:\t")
    n = int(n)
    stud = []

    for i in range(n):
        rno = input("Enter Roll No:\t")
        while not rno.isdigit():
            print("\nInvalid roll number.")
            rno = input("Enter Roll No:\t")
        rno = int(rno)

        # Check for duplicate roll number
        while any(student[0] == rno for student in stud):
            print("\nRoll number already exists.")
            rno = input("Enter Roll No:\t")
            while not rno.isdigit():
                print("\nInvalid roll number.")
                rno = input("Enter Roll No:\t")
            rno = int(rno)

        sname = input("Enter Student Name:\t")

        # Check English marks
        eng = input("Enter English Marks out of 100:\t")
        while not eng.isdigit():
            print("Invalid marks.")
            eng = input("Enter English Marks out of 100:\t")

        eng = int(eng)

        while eng < 0 or eng > 100:
            print("Marks must be between 0 and 100.")
            eng = input("Enter English Marks out of 100:\t")
            while not eng.isdigit():
                print("Invalid marks.")
                eng = input("Enter English Marks out of 100:\t")
            eng = int(eng)

        # Check Maths marks
        maths = input("Enter Maths Marks out of 100:\t")
        while not maths.isdigit():
            print("Invalid marks.")
            maths = input("Enter Maths Marks out of 100:\t")

        maths = int(maths)

        while maths < 0 or maths > 100:
            print("Marks must be between 0 and 100.")
            maths = input("Enter Maths Marks out of 100:\t")
            while not maths.isdigit():
                print("Invalid marks.")
                maths = input("Enter Maths Marks out of 100:\t")
            maths = int(maths)

        # Check Physics marks
        phy = input("Enter Physics Marks out of 100:\t")
        while not phy.isdigit():
            print("Invalid marks.")
            phy = input("Enter Physics Marks out of 100:\t")

        phy = int(phy)

        while phy < 0 or phy > 100:
            print("Marks must be between 0 and 100.")
            phy = input("Enter Physics Marks out of 100:\t")
            while not phy.isdigit():
                print("Invalid marks.")
                phy = input("Enter Physics Marks out of 100:\t")
            phy = int(phy)

        # Check Chemistry marks
        che = input("Enter Chemistry Marks out of 100:\t")
        while not che.isdigit():
            print("Invalid marks.")
            che = input("Enter Chemistry Marks out of 100:\t")

        che = int(che)

        while che < 0 or che > 100:
            print("Marks must be between 0 and 100.")
            che = input("Enter Chemistry Marks out of 100:\t")
            while not che.isdigit():
                print("Invalid marks.")
                che = input("Enter Chemistry Marks out of 100:\t")
            che = int(che)

        # Check IP marks
        IP = input("Enter IP Marks out of 100:\t")
        while not IP.isdigit():
            print("Invalid marks.")
            IP = input("Enter IP Marks out of 100:\t")

        IP = int(IP)

        while IP < 0 or IP > 100:
            print("Marks must be between 0 and 100.")
            IP = input("Enter IP Marks out of 100:\t")
            while not IP.isdigit():
                print("Invalid marks.")
                IP = input("Enter IP Marks out of 100:\t")
            IP = int(IP)

        stud.append([rno, sname, eng, maths, phy, che, IP])

    # Create DataFrame containing ALL students
    df = pd.DataFrame(stud,columns=["rno", "sname", "eng", "maths", "phy", "che", "IP"])
    #print("\n\nClass Record:\n============\n", df)
    df.to_csv(file_path,index=True)
    df.to_csv(file_path, index=False)
    report = pd.read_csv(file_path)
    print(report)
    print("\nCSV file successfully created and saved!! Exiting to the Main Menu!!\n")

#2
def details():
    c = 'y'
    while c == 'y':
        try:
            df = pd.read_csv(file_path)
        except FileNotFoundError:
            print("\nCSV file not found. Please create a Class Record first using option 1.")
            return

        df.set_index("rno", inplace=True)
        print(df)
        rno = input("Enter the Roll number of the student to see the total mark and percentage:\t")

        while not rno.isdigit():
            print("Invalid roll number.")
            rno = input("Enter the Roll number of the student to see the total mark and percentage:\t")

        rno = int(rno)

        while rno not in df.index:
            print("Roll number not found.")
            rno = input("Enter the Roll number of the student to see the total mark and percentage:\t")

            while not rno.isdigit():
                print("Invalid roll number.")
                rno = input("Enter the Roll number of the student to see the total mark and percentage:\t")

            rno = int(rno)

        rno = int(rno)

        total = 0
        for j in df.loc[:, "eng":"IP"]:
            total = total + df.at[rno, j]
        print("Name of the student:\t:", df.at[rno, 'sname'])
        print("Total marks obtained out of 500:\t", total)
        print("Percentage of marks:\t", (total / 500) * 100)

        c = input("\nDo you want to continue??? Press y or n:\t").lower()
        while c not in ['y', 'n']:
            print("Invalid option. Please enter y or n.")
            c = input("\nDo you want to continue??? Press y or n:\t").lower()
#3
def topbottom():
    while True:

        try:
            df = pd.read_csv(file_path)
        except FileNotFoundError:
            print("\nCSV file not found. Please create a Class Record first using option 1.")
            return

        df.set_index("rno", inplace=True)
        df["total"] = df.loc[:, "eng":"IP"].sum(axis=1)
        df = df.sort_values("total", ascending=False)

        print("\nDisplay Records Menu")
        print("1. Top Students")
        print("2. Bottom Students")
        print("3. Exit")

        ch3 = input("\nEnter choice:\t")
        while not ch3.isdigit() or int(ch3) not in [1, 2, 3]:
            print("Wrong Option")
            ch3 = input("\nEnter choice:\t")
        ch3 = int(ch3)

        if ch3 == 1:
            print(df.head(3))

        elif ch3 == 2:
            print(df.tail(3))

        elif ch3 == 3:
            break

#4
def modify():
    c = 'y'
    while c == 'y':
        try:
            df = pd.read_csv(file_path)
        except FileNotFoundError:
            print("\nCSV file not found. Please create a Class Record first using option 1.")
            return

        df.set_index("rno", inplace=True)
        print(df)
        print("\n\nOption to modify the data")
        print("=========================\n")
        no = input("Enter the roll number of the student to be modified:\t")
        while not no.isdigit():
            print("\nInvalid roll number.")
            no = input("Enter the roll number of the student to be modified:\t")

        no = int(no)

        while no not in df.index:
            print("\nRoll number not found.")
            no = input("Enter the roll number of the student to be modified:\t")

            while not no.isdigit():
                print("\nInvalid roll number.")
                no = input("Enter the roll number of the student to be modified:\t")

            no = int(no)

        sn = input("Enter the subject name (eng/maths/phy/che/ip):\t")

        # Check subject name
        while sn.lower() not in ["eng", "maths", "phy", "che", "ip"]:
            print("\nNo such subject")
            sn = input("Enter the subject name (eng/maths/phy/che/ip):\t")

        actual_column = "IP" if sn.lower() == "ip" else sn.lower()

        v = input("Enter the new value out of 100:\t")
        while not v.isdigit():
           print("Invalid marks.")
           v = input("Enter the new value out of 100:\t")

        v = int(v)

        while v < 0 or v > 100:
           print("Marks must be between 0 and 100.")
           v = input("Enter the new value out of 100:\t")
           while not v.isdigit():
               print("Invalid marks.")
               v = input("Enter the new value out of 100:\t")
           v = int(v)
        print("Old value:", df.at[no, actual_column])
        df.at[no, actual_column] = v
        print("\nUpdated data:")
        print(df)
        df.to_csv(file_path,index=True)
        print("\nCSV file successfully updated and saved!!")
        c = input("\nDo you want to continue??? Press y or n:\t").lower()
        while c not in ['y', 'n']:
            print("Invalid option. Please enter y or n.")
            c = input("\nDo you want to continue??? Press y or n:\t").lower()




#5
def visual():
    try:
        df=pd.read_csv(file_path)
    except FileNotFoundError:
        print("\nCSV file not found. Please create a Class Record first using option 1.")
        return

    df.set_index("rno", inplace=True)
    print(df)
    c='y'
    while (c=='y'):

        print("\n 1.HORIZONTAL BAR CHART")
        print("\n 2.VERTICAL BAR CHART" )
        print("\n 3.LINE CHART" )
        ch = input("\nEnter the choice:\t")

        while not ch.isdigit() or int(ch) not in [1, 2, 3]:
            print("Wrong Option")
            ch = input("\nEnter the choice:\t")

        ch = int(ch)

        no = input("\nEnter the roll number of the student:\t")
        while not no.isdigit() or int(no) not in df.index:
            print("Student not found")
            no = input("\nEnter the roll number of the student:\t")
        no = int(no)

        mark_list = []
        for j in df.loc[:, "eng":"IP"]:
            tmp = df.at[no, j]
            mark_list.append(tmp)

        if ch==1:                       
            x=["eng","maths","phy","che","IP"]
            c=['r','g','y','b','m']
            pl.barh(x,mark_list,color=c)
            pl.xlabel(df.at[no,"sname"])
            pl.ylabel("subject")
            pl.title ('MARK ANALYSIS')
            pl.show()


        elif ch==2:
            x=["eng","maths","phy","che","IP"]
            c=['r','g','y','b','m']
            pl.bar(x,mark_list,color=c)
            pl.xlabel(df.at[no,"sname"])
            pl.ylabel("mark")
            pl.title ('MARK ANALYSIS')
            pl.show()

        elif ch==3:
            x=["eng","maths","phy","che","IP"]
            pl.plot(x,mark_list,marker='D')
            pl.xlabel(df.at[no,"sname"])
            pl.ylabel("mark")
            pl.title ('MARK ANALYSIS')
            pl.show()

        c = input("\nDo you want to continue(Visualizing the data)??? Press y or n:\t").lower()
        while c not in ['y', 'n']:
            print("Invalid option. Please enter y or n.")
            c = input("\nDo you want to continue(Visualizing the data)??? Press y or n:\t").lower()

#main menu
while(True):
    print("\n\nMain Menu\n=========\n")
    print("1. Create a Class Record")
    print("2. Student wise Details")
    print("3. Top and Bottom Performances")
    print("4. Update the Details")
    print("5. Plot the data")
    print("6. Exit")
    ch = input("\nEnter your choice:\t")
    while not ch.isdigit() or int(ch) not in [1, 2, 3, 4, 5, 6]:
        print("Wrong Option")
        ch = input("\nEnter your choice:\t")
    ch = int(ch)
    if ch==1:
        data_csv()
    elif ch==2:
        details()
    elif ch==3:
        topbottom()
    elif ch==4:
        modify()
    elif ch==5:
        visual()
    elif ch==6:
        print("\nThank you for using the program..")
        print("Exiting The Program...")
        sys.exit()
        
    else:
        print("Wrong Option")
        


