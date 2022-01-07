import matplotlib.pyplot as plt
gdp_cap = [11415.80569, 2441.576404, 3025.349798, 2280.769906, 1271.211593, 469.70929810000007]
life_exp = [73.747, 74.249, 73.422, 62.698, 42.38399999999999, 43.487]
# Change the line plot below to a scatter plot
# plt.plot(gdp_cap, life_exp)
plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
plt.xscale('log')

# Show plot
plt.show()
