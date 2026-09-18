import pandas as pd
import matplotlib.pyplot as pl
import sys
#read the csv file
ipl_matches_df = pd.read_csv('C://CLASS 12 IP PROJECT//matches.csv')
#input
def get_choice():
    try:
        return int(input("Enter your choice:\t"))
    except ValueError:
        print("Invalid input. Please enter a valid choice.")
        return None
#view data
def view_data():
    print("\n1.View DataFrame")
    print("2.View the DataFrame Info")
    print("3.View Statistical Data")
    print("4.Show Columns")
    c=get_choice()
    if c==1:
        print(ipl_matches_df)
    elif c==2:
        ipl_matches_df.info()
    elif c==3:
        print(ipl_matches_df.describe())
    elif c==4:
        print(ipl_matches_df.columns)
    else:
      if c is not None:
         print("Invalid choice. Please enter a valid choice from 1 to 4.")         

#check NaN
def check_null():
    print("\n1.First Row without NaN value")
    print("2.Null value count")
    c=get_choice()
    if c==1:
        #the first index that doesn't contain a NaN value
        print("\nThe first row without a NaN value is: ",end="")
        print(ipl_matches_df.umpire3.first_valid_index())
    elif c==2:
        #null values count
        print("\nColumn-wise NaN values count:\n")
        print(ipl_matches_df.isnull().sum())
    else:
      if c is not None:
         print("Invalid choice. Please enter a valid choice (1 or 2).") 
        
#win per season
def win():
    print("\n1.Most wins in each season")
    print("2.Win per season")
    c=get_choice()
    if c==1:
        # team with the most wins in each season
        year = 2008
        teams_per_season = 	ipl_matches_df.groupby('season')['winner'].value_counts()
        most_wins_df = pd.DataFrame(columns=['year', 'team', 'wins'])
        print("\nWINS PER SEASON\n===============\n")
        for items in teams_per_season.items():    
            if items[0][0]==year:
                #print(items)
                win_series = pd.DataFrame({
                	'year': [items[0][0]],
                	'team': [items[0][1]],
               	        'wins': [items[1]],})
                most_wins_df = pd.concat([most_wins_df,win_series])
                year += 1
        print(most_wins_df)
    elif c==2:
        #win per season
        teams_per_season = ipl_matches_df.groupby('season')['winner'].value_counts()
        print(teams_per_season)
    else:
        if c is not None:
          print("Invalid choice. Please enter a valid choice(1 or 2).")
              
#visualization
def graph():
    print("\n1.Visualize win per season")
    print("2.Visualize venue hosted maximum games")
    print("3.Visualize most successful team")
    c=get_choice()
    if c==1:
        #create DataFrame for win per season
        year=2008
        teams_per_season=ipl_matches_df.groupby('season')['winner'].value_counts()
        win_per_season_df=pd.DataFrame(columns=['year', 'team','wins'])
        print("\nWINS PER SEASON\n===============\n")
        for items in teams_per_season.items():    
            if items[0][0]==year:
               	 #print(items)
               	 win_series = pd.DataFrame({'year': [items[0][0]],\
                                            'team': [items[0][1]],\
                                            'wins': [items[1]]})
               	 win_per_season_df = pd.concat([win_per_season_df,win_series])
               	 year+=1
	#visualization
        pl.barh(win_per_season_df.team,win_per_season_df.wins,\
        height=0.5,\
        color=['r','g','b','k','y','c','m','g','b','k','y','c'])
        pl.xlabel("Wins")
        pl.ylabel("Teams")
        pl.title("Season Winning")
        pl.show()
        
    elif c==2:
        #venue hosted max games
        venue_ser = ipl_matches_df['venue'].value_counts()
        venue_df = pd.DataFrame(columns=['venue', 'matches'])
        for items in venue_ser.items():
            temp_df = pd.DataFrame({
                'venue':[items[0]],
                'matches':[items[1]]
            })
            venue_df =pd.concat([venue_df,temp_df],ignore_index=True)
        #print(venue_df)

        #venue visualization
        c=list("rgbkycmyrgbkycmyrgbkycmyrgbkycmyrgbkycmyk")
        pl.bar(venue_df.venue,venue_df.matches,color=c)
        pl.xlabel("Stadium Name")
        pl.ylabel("Number of matches")
        pl.title("Hosted Matches by stadiums")
        pl.xticks(rotation=90)
        pl.grid(True)
        pl.show()
    elif c==3:
        #most successful teams
        team_wins_ser = ipl_matches_df['winner'].value_counts()
        team_wins_df = pd.DataFrame(columns=["team", "wins"])
        for items in team_wins_ser.items():
            temp_df1 = pd.DataFrame({
                'team':[items[0]],
                'wins':[items[1]]
            })
            team_wins_df = pd.concat([team_wins_df,temp_df1], ignore_index=True)
        #print(team_wins_df)

        #DV most successful teams
        c=list("rgbkycmcygrmkygb")
        pl.bar(team_wins_df.team,team_wins_df.wins,color=c)
        pl.xlabel("Team")
        pl.ylabel("Wins")
        pl.title("Most Successful Teams")
        pl.xticks(rotation=90)
        pl.grid(True)
        pl.show()
    else:
        if c is not None:
          print("Invalid choice. Please enter a valid choice from 1 to 3.")
#umpire details
def umpire():
    print("\n1.Umpire officiated most IPL matches")
    print("2.Top 5 Umpires")
    c=get_choice()
    if c==1:
        #umpire details - which umpire officiated the most IPL matches
        umpire1_ser = ipl_matches_df['umpire1'].value_counts()
        umpire2_ser = ipl_matches_df['umpire2'].value_counts()
        umpires_df = pd.concat([umpire1_ser, umpire2_ser], axis=1)
        umpire_ser = umpires_df.sum(axis=1)
        print(umpire_ser.sort_values(ascending=False).head(1).astype(int))
    
    elif c==2:
        #top 5 umpires officiated the matches
        umpire1_ser = ipl_matches_df['umpire1'].value_counts()
        umpire2_ser = ipl_matches_df['umpire2'].value_counts()
        umpires_df = pd.concat([umpire1_ser, umpire2_ser], axis=1)
        umpire_ser = umpires_df.sum(axis=1)
        umpire_df = pd.DataFrame(columns=["umpire", "matches"])
        for items in umpire_ser.items():
            temp_df4 = pd.DataFrame({
                'umpire':[items[0]],
                'matches':[items[1]]
            })
            umpire_df= pd.concat([umpire_df,temp_df4], ignore_index=True)
        print(umpire_df.sort_values('matches', ascending=False).head())
    else:
        if c is not None:
          print("Invalid choice. Please enter a valid choice(1 or 2).")
#main menu
def main():
    while True:
        print("\nAnalysing IPL Data\n==================\n")
        print("Main Menu\n=========\n")
        print("1.View the Data")
        print("2.Check for NaN values")
        print("3.Win per season")
        print("4.Data Visualization")
        print("5.Umpire Details")
        print("6.Exit")
        ch=get_choice()
        if ch==1:
            view_data()
        elif ch==2:
            check_null()
        elif ch==3:
            win()
        elif ch==4:
            graph()
        elif ch==5:
            umpire()
        elif ch==6:
            print("\nThank you for using the program.")
            print("Exiting The Program...")
            sys.exit()
        else:
             if ch is not None:
                print("Invalid choice. Please enter a number from 1 to 6.")
             
main()

