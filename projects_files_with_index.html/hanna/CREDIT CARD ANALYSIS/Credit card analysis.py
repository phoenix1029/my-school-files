#   project name        : credit card analysis
import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame()
csv_file = "C:\\PROJECT\\BankChurners (1).csv""


def read_csv_file():
    df = pd.read_csv(csv_file)
    print(df)

# name of function      : clear
# purpose               : clear output screen


def clear():
    for x in range(65):
               print()

# name of function      : data_analysis_menu
# purpose               : To analysis the data from csv file

def data_analysis_menu():
        df = pd.read_csv(csv_file)
        while True:
            clear()
            print('D A T A   A N A L Y S I S   M E N U  ')
            print('-'*50,'\n')
            print('1.   Show Whole DataFrame')
            print('2.   Show Columns')
            print('3.   Row Top Rows')
            print('4.   Row Bottom Rows')
            print('5.   Show Specific Column')
            print('6.   Add a New Record')
            print('7.   Add a New Column')
            print('8.   Delete a Column')
            print('9.   Delete a Record')
            print('10.  Card Type User')
            print('11.  Gender wise User')
            print('12.  Data Summary')
            print('13.  Exit (Move to main menu)')
            ch = int(input('\n\nEnter your choice:\t'))
            if ch == 1:
                print(df)
                wait = input('\n Press any key to continue.....')
            if ch == 2:
                print(df.columns)
                wait = input('\n Press any key to continue.....')
            if ch == 3:
                n = int(input('Enter Total rows you want to show :'))
                print(df.head(n))
                wait = input('\n Press any key to continue.....')
            if ch == 4:
                n = int(input('Enter Total rows you want to show :'))
                print(df.tail(n))
                wait = input('\n Press any key to continue.....')
            if ch == 5:
                print(df.columns)
                col_name =str( input('Enter Column Name that You want to print : '))
                print(df[col_name])
                wait = input('\n Press any key to continue.....')
            if ch == 6:
                a = input('Enter Customer ID :')
                b = input('Enter Customer Type :')
                c = input(' Enter Customer Age:')
                d = input('Enter Customer Gender :')
                e = input('Enter Customer Dependent Count :')
                f = input('Enter Education Level :')
                g = input('Enter Marital Status :')
                h = input('Enter Income Category :')
                i = input('Enter Card Category :')
                j = input('Enter Month on Book')
                k = input('Enter Total Relationship count :')
                l = input('Enter Total Month Inactive in last 12 month  :')
                m = input('Enter Total Contacted in last 12 months :')
                n = input('Enter Credit Limit :')
                o = input('Enter Revolving Balance :')
                p = input('Enter Average Open to Buy Card :')
                q = input('Enter Total amount change Q4 to Q1 :')
                r = input('Enter Total Transaction amount :')
                s = input('Enter Total Transaction Credit:')
                t = input('Enter Total Credit Change Q4 Q1 :')
                u = input('Enter Average Utilization Ratio  :')
               #dictionary
                data = {
	'clientID': a, 'Type': b, 'age': c,'gender': 	d,'Dependent_count': e, 	'Educational_Level': f,'Marital_Status': g,                      			'Income_Category':h,'Card_Category':i,'Months_on_book':j,'Total_Re	lationship_count':k,                      	'Month_Inactive_12_month':l,'Contacts_count_12_mon':m,'Credit_L	imit':n,                      	'Total_Revolving_Bal':o,'Avg_Open_To_Buy':p,'Total_Amt_chng_Q4_	Q1':q,'Total_Trans_Amt':r,                       	'Total_Trans_Ct':s,'Total_Ct_Chng_Q4_Q1':t,'Average_Utilization_Rat	ion':u
                        }
                df = df._append(data, ignore_index=True)
                print(df)
                wait = input('\n Press any key to continue.....')
            if ch == 7:
                col_name = input('Enter new column name :')
                col_value = int(input('Enter default column value :'))
                df[col_name] = col_value
                print(df)
                print('\n Press any key to continue....')
                wait = input()

            if ch == 8:
                col_name = input('Enter column Name to delete :')
                del df[col_name]
                print(df)
                print('\n Press any key to continue....')
                wait = input()

            if ch == 9:
                index_no = int(input('Enter the Index Number that You want to 		delete :'))
                df = df.drop(df.index[index_no])
                print(df)
                print('\n Press any key to continue....')
                wait = input()

            if ch == 10:
                print(df.columns)
                print(df['Type'].unique())
                tipe = input('Enter Card Type :')
                g = df.groupby('Type')
                print('Card Type : ', tipe)
                print(g['Type'].count())
                print('\n Press any key to continue....')
                wait = input()

            if ch == 11:
                df1 = df.Gender.unique()
                print('Available Gender :', df1)
                print('\n\n')
                schName = input('Enter Gender Type :')
                df1 = df[df.Gender == schName]
                print(df1)
                print('\n Press any key to continue....')
                wait = input()

            if ch == 12:
                print(df.describe())
                print("\nPress any key to continue....")
                wait = input()
            if ch == 13:
                break


# name of function      : graph
# purpose               : To generate a Graph menu
def graph():
    df = pd.read_csv(csv_file)
    while True:
        clear()
        print('\nGRAPH MENU ')
        print('-'*50)
        print('1.  Whole Data LINE Graph\n')
        print('2.  Whole Data Bar Graph\n')
        print('3.  Bar Graph By Education Level\n')
        print('4.  Bar Graph By Income Level\n')
        print('5.  Exit (Move to main menu)\n')
        ch = int(input('Enter your choice:\t'))

        if ch == 1:
            g = df.groupby('Gender')
            x = df['Gender'].unique()
            y = g['Gender'].count()
            #plt.xticks(rotation='vertical')
            plt.xlabel('Gender')
            plt.ylabel('Total Credit Card Users')
            plt.title('Credit Card User- Gender wise')
            plt.grid(True)
            plt.plot(x, y)  #line graph
            plt.show()

        if ch == 2:
            g = df.groupby('Gender')
            x = df['Gender'].unique()
            y = g['Gender'].count()
            #plt.xticks(rotation='vertical')
            plt.xlabel('Gender')
            plt.ylabel('Total Credit Card Users')
            plt.title('Credit Card User- Gender wise')
            plt.bar(x, y)  #bar graph
            plt.grid(True)
            plt.show()
            wait = input()

        if ch == 3:
            g = df.groupby("Education_Level")
            x = df['Education_Level'].unique()
            y = g['Education_Level'].count()
            plt.bar(x, y)
            #plt.xticks(rotation='vertical')
            plt.grid(True)
            plt.title('Education Level wise Card User')
            plt.xlabel('Education Level')
            plt.show()
            wait = input()

        if ch == 4:
            g = df.groupby("Income_Category")
            x = df['Income_Category'].unique()
            y = g['Income_Category'].count()
            plt.grid(True)
            plt.title('Credit Card User- Income Group')
            plt.xlabel('Income Group')
            plt.ylabel('Card Users')
            plt.bar(x,y)
            plt.show()

        if ch == 5:
            break


# function name          : export_menu
# purpose                : function to generate export menu
def export_menu():
    df = pd.read_csv(csv_file)
    while True:
        clear()
        print('\n\nEXPORT MENU ')
        print('-'*50)
        print()
        print('1.  CSV File\n')
        print('2.  Excel File\n')
        print('3.  Exit (Move to main menu)')
        ch = int(input('Enter your Choice :\t '))

        if ch == 1:
            df.to_csv('C:\\PROJECT\\BankChurners (1).csv')
            print('\n\nCheck your new file "bankchurner_backup.csv"  on E: 	Drive.....')
            wait =input('\n Press any key to continue.....')

        if ch == 2:
            df.to_excel('C:\\PROJECT\\BankChurners (1).xlsx')
            print('\n\nCheck your new file "bankchurner_backup.xlsx"  on E: 	Drive.....')
            wait = input('\n Press any key to continue.....')

        if ch == 3:
            break

#main menu function
def main_menu():
    clear()
    while True:
        clear()
        print('MAIN MENU ')
        print('-'*50)
        print()
        print('1.  Read CSV File\n')
        print('2.  Data Analysis Menu\n')
        print('3.  Graph Menu\n')
        print('4.  Export Data\n')
        print('5.  Exit\n')
        choice = int(input('Enter your choice :\t'))

        if choice == 1:
            read_csv_file()
            wait = input('\n\n Press any \ney to continue....')

        if choice == 2:
            data_analysis_menu()
            wait = input('\n\n Press any \ney to continue....')

        if choice == 3:
            graph()
            wait = input('\n\n Press any \ney to continue....')
        if choice == 4:
            export_menu()
            wait = input('\n\n Press any \ney to continue....')

        if choice == 5:
            brea\n
        clear()
           

# call your main menu
main_menu()
