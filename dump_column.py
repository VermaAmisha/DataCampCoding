# Apply json.loads to the bird_facts column and transform it to a list 
birds_facts = birds['bird_facts'].apply(json.loads).to_list()

# Convert birds_facts into a JSON 
birds_dump = json.dumps(birds_facts)

# Print birds_dump
print(birds_dump)
