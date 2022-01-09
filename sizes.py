import matplotlib.pyplot as plt
# Import numpy as np
import numpy as np

pop = pop = [2.517, 3.692, 5.263, 6.972]
gdp_cap = [ 3025.349798, 2280.769906, 1271.211593, 469.70929810000007]
life_exp = [73.422, 62.698, 42.38399999999999, 43.487]

# Store pop as a numpy array: np_pop
np_pop = np.array(pop)

# to make the dots in different sizes to show different population data

# Double np_pop
np_pop = np_pop * 2

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()
