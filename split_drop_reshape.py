# Split main_title by a colon and assign it to two columns named title and subtitle 
books_sh[['title', 'subtitle']] = books_sh['main_title'].str.split(':', expand=True)

# Split version by a space and assign the second element to the column named volume 
books_sh['volume'] = books_sh['version'].str.split(' ').str.get(1)

# Drop the main_title and version columns modifying books_sh
books_sh.drop(['main_title', 'version'], axis=1, inplace=True)

# Reshape using title, subtitle and volume as index, name feature the new variable from columns starting with number, separated by undescore and ending in words 
sh_long = pd.wide_to_long(books_sh, stubnames='number', i=['title', 'subtitle', 'volume'], 
                  j='feature', sep='_', suffix='\w+')

# Print sh_long 
print(sh_long)
