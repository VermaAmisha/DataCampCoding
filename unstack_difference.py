# Unstack the third level and calculate the difference between columns
obesity_variation = obesity.unstack(level = 2).diff(axis = 1)

# Print obesity_variation
print(obesity_variation)
