from Ratings.helperFunctions import plot_position_stat_bar,plot_player_stat_by_week,get_player_stats,get_season_totals_by_position


'ran through - lost their touch - not how they used to be- out of their prime'
'this player is on the decline'
'1 games played- indicates their health and availability'
'2 rushing yards - indiactes their athleticism, how nim,ble a player'
'3 td- Not a lot of completed passes made, not getting in the redzone so a touchdown is possible, games played'
'4'

qbStats = get_season_totals_by_position(2024,'QB')
print(qbStats)


WentzStats=get_player_stats(2024,'Carson,''Wentz')
plot_player_stat_by_week(2024,'Carson,''Wentz',"passing_yards,"save_path='Jalen Hurts Passing Yards 2024')

'Carson Wentz best season was from 2019 with the Philadelphia Eagles. He passed for over 4000 yards becoming the first Eagles quarterback to do so'
' The reason Wentz is washed however is his massive decline of passing yards, games played and the amount of teams he has been with since the Eagles '



