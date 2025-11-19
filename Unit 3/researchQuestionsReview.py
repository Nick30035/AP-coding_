from helperLogic import get_player_stats_by_name, plot_weekly_player_stats,plot_player_stat, get_team_records, get_advanced_team_records, get_position_columns, get_season_Results_By_team , weeklyPlayerStats
import matplotlib.pyplot as plt

# Columns available to research based on year and position
# columnData = get_position_columns(2024, "QB")
# print(columnData)

'1. How much does QB pass accuracy influence team wins ? '
# teamRecord = get_team_records(2024)
# print(teamRecord)

# qbData = weeklyPlayerStats(2024, 'QB')
# print(qbData)

'J.Allen'
'J.Hurts'

# playerStat= get_player_stats_by_name(2024,'J. Hurts','QB')
# print(playerStat)

'Answer: Yes, there is a relationship. based on the average qb completion %, anything above 60 % is considered a good completion number'
"also based on team records, the top 10- top teams all have had qbs that have over 65% completion percentages."


'2. Does defensive turnovers contribute to a teams win percentage ? '
advanceStates = get_advanced_team_records(2024)
print(advanceStates)

'This question is measurable, it allows me to use data an order to get my answer'
'Using the advanceStates function, it provided me with advanced stats for team. Analyzing the category of'
'defensive turnovers, the Lions who finished the season with a record of 15-2 had the most turnovers'
'and highest win percentage.'



'3. Who has the most passing yards of all time ? '

'I cannot answer this question because it is too board'
'When using the helperfunctions teamstats and year, it only allows you to go back so far'
'which limits the amount of data you can get.'

