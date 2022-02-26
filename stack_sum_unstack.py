# Stack the first level, get sum, and unstack the second level
obesity_sum = obesity.stack(level = 0).sum(axis = 1).unstack(level = 1)

# Print obesity_max
print(obesity_sum)
