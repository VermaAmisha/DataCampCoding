# Unstack the first level and calculate the mean of the columns
obesity_general = obesity.unstack(level=0).mean(axis = 1)

# Print obesity_general
print(obesity_general)
