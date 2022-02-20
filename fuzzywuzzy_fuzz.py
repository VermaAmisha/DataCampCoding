from fuzzywuzzy import fuzz

print(fuzz.WRatio('italian vs american', 'american vs asian' , 'italian vs asian'))
