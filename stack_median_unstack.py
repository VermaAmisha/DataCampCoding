# Stack obesity, get median of columns and unstack again
median_obesity = obesity.stack().median(axis = 1).unstack()

# Print median_obesity
print(median_obesity)
