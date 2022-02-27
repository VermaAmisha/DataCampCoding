# Explode the values of bounds to a separate row
obesity_bounds = obesity['bounds'].explode()

# Merge obesity_bounds with country and perc_obesity columns of obesity using the indexes
obesity_final = obesity[['country', 'perc_obesity']].merge(obesity_bounds, 
                                        right_index= True, 
                                        left_index = True)

# Print obesity_final
print(obesity_final)
