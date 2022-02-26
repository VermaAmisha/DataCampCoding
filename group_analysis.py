# Stack country level, group by country and get the mean
obesity_mean = obesity.stack(level='country').groupby('country').mean()

# Print obesity_mean
print(obesity_mean)
