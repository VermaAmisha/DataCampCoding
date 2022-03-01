# Import the json_normalize function
from pandas import json_normalize

# Normalize movies and separate the new columns with an underscore 
movies_norm = json_normalize(movies, sep='_')

# Reshape using director and producer as index, create movies from column starting from features
movies_long = pd.wide_to_long(movies_norm, stubnames='features', 
                      i=['director','producer'], j='movies', 
                      sep='_', suffix='\w+')

# Print movies_long
print(movies_long)
