import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import time
global df
filepath="C:/Users/shreya/Downloads/project_files/projects/analeena/LITERACY RATE ANALYSIS/project.csv"
try:
    df=pd.read_csv(filepath)
except FileNotFoundError:
    print("CSV file not found. Please make sure project.csv is present in the required location.")
    sys.exit()
df.set_index('State/UTs',inplace=True)
#-----------------------------------------------------------------
#Function to display the main menu.
#-----------------------------------------------------------------
def MainMenu():
    ans='y'
    while ans=='y' or ans=='Y':
        opt=''
        print()
        print('========================================================')
        print('             Literacy Rate of India                     ')
        print('********************************************************')
        print('1-Data Visualisation\n')
        print('2-Analysis\n')
        print('3-Exit')
        print('========================================================')
        opt=input('Enter your choice:')
        while opt not in ['1','2','3']:
            print("Invalid choice. Please enter 1, 2 or 3.")
            opt=input('Enter your choice:')
        if opt=='1':
            visuals()
        elif opt=='2':
            analysis()
        elif opt=='3':
            my_chance=input('Do you really wnat to exit?(y/n)')
            while my_chance not in ['y','Y','n','N']:
                print("Invalid input. Please enter Y or N.")
                my_chance=input('Do you really want to exit?(y/n)')
            if my_chance.lower=='y':
                print("Thank you for using the program.")
                print('Exiting The Program...')
                sys.exit()
            else:
                continue
        else:
            ans=input('Do you want to continue(y/n)')
#--------------------------------------------------------------------
def visuals():
    df=pd.read_csv(filepath)
    print(df)
    while True:
        print("Year's in this analysis are 1951,1961,1971,1981,1991,2001,2011")
        print()
        print('V I S U A L   M E N U')
        print('=====================')
        print('1-Line chart of a particular year')
        print('2-Bar chart of a particular  year')
        print('3-Histogram for a year')
        print('4-Line Chart Average Literacy Year wise')
        print('5-Back to Main Menu')
        print('======================================')
        choice=input('enter your choice:')
        while choice not in ['1','2','3','4','5']:
            print("Invalid choice. Please enter a number from 1 to 5.")
            choice=input('enter your choice:')
        choice=int(choice)
        if choice==1:
            year=input('Enter Year Of Literacy:')
            while year not in ['1951','1961','1971','1981','1991','2001','2011']:
                print("Invalid year. Please enter one of: 1951, 1961, 1971, 1981, 1991, 2001 or 2011.")
                year=input('Enter Year Of Literacy:')
            plt.plot(df['State/UTs'],df[year])
            plt.xlabel('state/UT Name -->',color='r',fontsize=12)
            plt.ylabel('Literacy Rate (%)->',color='r',fontsize=12)
            plt.title('TopIndian States Literacy Analysis',color='g',fontsize=16)
            plt.xticks(rotation=90)
            plt.tight_layout()
            plt.show()
        elif choice==2:
            year=input('Enter Year Of Literacy:')
            while year not in ['1951','1961','1971','1981','1991','2001','2011']:
                print("Invalid year. Please enter one of: 1951, 1961, 1971, 1981, 1991, 2001 or 2011.")
                year=input('Enter Year Of Literacy:')
            plt.bar(df['State/UTs'],df[year])
            plt.xlabel('state/UT Name -->',color='r',fontsize=12)
            plt.ylabel('Literacy Rate (%)->',color='r',fontsize=12)
            plt.title('TopIndian States Literacy Analysis',color='g',fontsize=16)
            plt.xticks(rotation=90)
            plt.tight_layout()
            plt.show()
        elif choice==3:
            year=input('Enter Year of Literacy:')
            while year not in ['1951','1961','1971','1981','1991','2001','2011']:
                print("Invalid year. Please enter one of: 1951, 1961, 1971, 1981, 1991, 2001 or 2011.")
                year=input('Enter Year of Literacy:')
            df.hist(column=year,color='r',edgecolor='black')
            plt.xlabel('Literacy Rate (%)',color='r',fontsize=12)
            plt.ylabel('Number of States/UTs',color='r',fontsize=12)
            plt.title(f'Literacy Rate Distribution ({year})',color='g',fontsize=16)
            plt.tight_layout()
            plt.show()
        elif choice==4:
            year_cols=['1951','1961','1971','1981','1991','2001','2011']
            sl=df[year_cols].mean()

        
            
            #sl=df.mean()
            mylabel=sl.index
            plt.plot(mylabel,sl.values,linestyle='dashed',linewidth=3,color='r',marker='o',\
                     mfc='b',ms=10)
            plt.xlabel('Year-->',color='b',fontsize=12)
            plt.ylabel('Literacy Rate (%)->',color='b',fontsize=12)
            plt.title('Indian Literacy Analysis 1951 to 2011',color='r',fontsize=16)
            plt.grid()
            plt.show()
        elif choice==5:
             break
        else:
             print("Invalid number. Please enter a positive whole number.")
#-------------------------------------------------------------
#Function to analyse data from a dataframe.
#-------------------------------------------------------------
def analysis():
    df=pd. read_csv(filepath)
    df.set_index('State/UTs', inplace=True)
    while True:
        print('\nDataFrame Analysis')
        print('******************')
        menu='''\n1.Top record
\n2.Bottom records
\n3.To Display Literacy of a particular year
\n4.To Display states with Maximum Literacy rate
\n5.To Display Average Literacy of India
\n6.To Display Complete DataFrame
\n7.Back to Main Menu'''
        print(menu)
        print('=================================================================')
        ch_an=input('Enter your choice:')
        while ch_an not in ['1','2','3','4','5','6','7']:
            print("Invalid number. Please enter a positive whole number.")
            ch_an=input('Enter your choice:')
        ch_an=int(ch_an)
        if ch_an==1:
            n=input('Enter the number of records to be displayed:')
            while not n.isdigit() or int(n)<=0:
                print("Invalid year. Please enter one of: 1951, 1961, 1971, 1981, 1991, 2001 or 2011.")
                n=input('Enter the number of records to be displayed:')
            n=int(n)
            print('Top',n,'records from the dataframe')
            print(df.head(n))
        elif ch_an==2:
            n=input('Enter the number of records to be displayed:')
            while not n.isdigit() or int(n)<=0:
                print("Invalid number. Please enter a positive whole number.")
                n=input('Enter the number of records to be displayed:')
            n=int(n)
            print('Bottom',n,'records from the dataframe')
            print(df.tail(n))
        elif ch_an==3:
            print('Name of the column\n',df.columns)
            col=input("Enter the year of literacy:")
            while col not in ['1951','1961','1971','1981','1991','2001','2011']:
                print("Invalid choice.")
                col=input("Enter the year of literacy:")
            print(df[col])
        elif ch_an==4:
            yr=input('Enter year:')
            while yr not in ['1951','1961','1971','1981','1991','2001','2011']:
                print("Invalid choice.")
                yr=input('Enter year:')
            print()
            print('State with Maximum Literac in the year-'+yr)
            print('----------------------------------------------\n')
            x=df[yr].max()
            print(df.loc[(df[yr]==x),[yr]].reset_index())
            print('---------------------------------------------------------\n')
        elif ch_an==5:
            print('Average Literacy of India')
            print('--------------------------')
            #print(df.mean())
            print(df.mean(numeric_only=True))
            print('--------------------------')
        elif ch_an==6:
            print('Displaying complete DataFrame')
            print('-----------------------------')
            print(df)
            print('------------------------------')
        
        elif ch_an==7:
            break
        else:
            print("Invalid choice.")

MainMenu()
