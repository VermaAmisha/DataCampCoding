# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch

for i,h in enumerate(house):
    # print(str(h[i]) + " is " + str(h[i] )+ "sqm")
    print("the " + h[0] + " is " + str(h[1]) + " sqm")
