from helperFunctions import weeklyPlayerStats, plot_weekly_player_stats, plot_player_stat
import matplotlib.pyplot as plt

# 1) Using an existing stats dataframe:
stats = weeklyPlayerStats(2024, "RB")  
print(stats)
plot_player_stat(stats, stat="rushing_yards", top_n=10, title=" RB rushing yards (2024)", save_path="RB_rushing_yards_2024.png"  )

# 2) One-liner wrapper:
plot_weekly_player_stats(2024, "RB", stat="rushing_yards", top_n=15, week=[1,2,3], save_path="wr_rushing_tds_wk1-17.png")

# Use the new plot_player_stat() and plot_weekly_player_stats() to visualize the data into bar graphs and answer the following questions.

# 1. Use each helper function to find your own metric to visualize. use the weeklyPlayerStats function to find positions and stat columns by name
 #  I created a graph showing the most rushing yards by a RB, S. Barkley 2504
# 2. Find the player with the most touchdowns in 2024?
# J.Gibbs
# 3. find the player with the highest total passing yards in 2024.
#J. Goff 4942
# 4. which player had the highest rushing yards in week 1 and in week 17?
# D. Henry Week 1 S. Barkley Week 17