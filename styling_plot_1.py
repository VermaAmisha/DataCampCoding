import matplotlib.pyplot as plt

# Use the "ggplot" style and create new Figure/Axes
plt.style.use("ggplot")
fig , ax = plt.subplots()
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])
plt.show()
