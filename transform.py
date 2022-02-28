# Transform the list-like column named bounds  
obesity_explode = obesity.explode('bounds')

# Modify obesity_explode by resetting the index 
obesity_explode.reset_index(drop=True, inplace=True)

# Print obesity_explode
print(obesity_explode)
