# Concatenate the title and subtitle separated by "and" surrounded by spaces
hp_books['full_title'] = hp_books['title'].str.cat(hp_books['subtitle'], sep =" and ") 

# Split the authors into writer and illustrator columns
hp_books[['writer', 'illustrator']] = hp_books['authors'].str.split('/', expand=True)

# Melt goodreads and amazon columns into a single column
hp_melt = hp_books.melt(id_vars=['full_title', 'writer'],
                        var_name='source', 
                        value_vars=['goodreads', 'amazon'], 
                        value_name='rating')

# Print hp_melt
print(hp_melt)
