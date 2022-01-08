import matplotlib.pyplot as plt
import numpy as np

gdp_cap = [11415.80569, 2441.576404, 3025.349798, 2280.769906, 1271.211593, 469.70929810000007]
life_exp = [73.747, 74.249, 73.422, 62.698, 42.38399999999999, 43.487]
pop = [26.084662, 85.262356, 4.018332, 22.211743, 11.746035, 12.311143]
col = ['blue', 'red', 'blue', 'yellow', 'blue', 'green']

# to give different color to plot of different dots
# alpha for opacity of the dots

# Specify c and alpha inside plt.scatter()
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2,c= col, alpha=0.8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Add grid() call
plt.grid(True)

# Show the plot
plt.show()
