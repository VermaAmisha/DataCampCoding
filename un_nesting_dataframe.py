# Define birds reading names and bird_facts lists into names and bird_facts columns
birds = pd.DataFrame(dict(names=names, bird_facts=bird_facts))

# Apply to bird_facts column the function loads from json module
data_split = birds['bird_facts'].apply(json.loads).apply(pd.Series)

# Remove the bird_facts column from birds
birds = birds.drop(columns='bird_facts')

# Concatenate the columns of birds and data_split
birds = pd.concat([birds,  data_split], axis=1)

# Print birds
print(birds)
