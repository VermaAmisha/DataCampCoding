# Set the argument to get the maximum for each row and column
fifa_mean = fifa_players.pivot_table(index=['nationality', 'club'], 
                                     columns='year', 
                                     aggfunc='max',
                                     margins= True)

# Print fifa_mean
print(fifa_mean)
