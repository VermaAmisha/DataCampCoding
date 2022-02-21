# Pivot fifa_players to get overall and attacking scores indexed by name and identified by movement
fifa_over_attack = fifa_players.pivot(index='name', 
                                     columns='movement', 
                                     values=['overall', 'attacking'])

# Print fifa_over_attack
print(fifa_over_attack)
