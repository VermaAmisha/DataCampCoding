# Stack country level, group by country and get the median 
obesity_median = obesity.stack(level = 'country').groupby('country').median()

# Print obesity_median
print(obesity_median)
