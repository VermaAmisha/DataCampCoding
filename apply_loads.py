# Apply json.loads to the bird_facts column and transform it to a list
birds_facts = birds['bird_facts'].apply(json.loads).to_list

# Print birds_facts
print(birds_facts)
