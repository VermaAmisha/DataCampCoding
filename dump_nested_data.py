# Apply json.loads to the bird_facts column and transform it to a list 
birds_facts = birds['bird_facts'].apply(json.loads).to_list()

# Convert birds_fact into a JSON 
birds_dump = json.dumps(birds_facts)

# Read the JSON birds_dump into a DataFrame
birds_df = pd.read_json(birds_dump)

# Concatenate the 'names' column of birds with birds_df 
birds_final = pd.concat([birds['names'], birds_df], axis=1)

# Print birds_final
print(birds_final)
