# Specify director and producer to use as metadata for each record 
normalize_movies = json_normalize(movies, 
                                  record_path='features', 
                                  meta=['director','producer'])

# Print normalize_movies
print(normalize_movies)
