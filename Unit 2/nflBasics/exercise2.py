import pandas as pd

import nfl_data_py as nfl


from helperFunctions import get_team_records, get_season_Results_By_team, weeklyPlayerStats

##schedules = nfl.import_schedules([2025])

#print(schedules.columns.tolist())

#records =get_team_records(2025)

#birds = get_season_Results_By_team(2025,'')
#print(birds)
##pd = [4, 3 ,7, 6, -4, 17]
-1

# COLTS AND BUCS FOR HIGHEST PD
# COLTS 78
# BUCS 14

#top6_Teams = ['TB,''IND','LA,''BUF','SF','SEA,''PIT']
#Which team has the best point differential this season?
'The best overall PD is...'
'TB'
'IND'


#team_1= get_season_Results_By_team(2025,'TB')#14 PD
#team_2=get_season_Results_By_team(2025,'IND')# 78 PD
#team_3=get_season_Results_By_team(2025,'LA')
#team_4=get_season_Results_By_team(2025,'BUF')# 7
#team_5=get_season_Results_By_team(2025,'SF')
#team_6=get_season_Results_By_team(2025,'SEA')

# formula for PD = points for - points against

##print(team_1)
#print(team_2)
#print(team_3)
#print(team_4)
#print(team_5)
#print(team_6)

#Which team has the worst point differential this seaosn?
'The worst PD is IND. They have a point differential of 78 points'
''

#Which team has the best home point differential season?
'The best home PD is... IND - 64'

#Which team has the best away point differential this season?
'The best away PD is '
def pdCheck():
    print("Please enter a number")
    number= input()
    values = []

    while number != 'q':
        values.append(int(number))
        print(values)
        print("please enter a number")
        number = input()
    else:
     print('doing calculation') 
     total = sum(values)
    print(total)
        
     #For loop
     # Add all the numbers and return the sum of the numbers.
     # this should give us the PD
     # HINT : you're going to be using a for loop

pdCheck()









