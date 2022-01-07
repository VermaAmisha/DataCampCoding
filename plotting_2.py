# Import package
import matplotlib.pyplot as plt
pop = [3.447496, 26.084662, 85.262356, 4.018332, 22.211743, 11.746035, 12.311143]
life_exp = [76.384, 73.747, 74.249, 73.422, 62.698, 42.38399999999999, 43.487]

# Build plot
plt.plot(pop,life_exp)

# Show plot
plt.show()

# Build Scatter plot
plt.scatter(pop,life_exp)

# Show plot
plt.show()
