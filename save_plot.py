import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# Save as a PNG file
fig.savefig("my_figure.png")

# Save as a PNG file with 300 dpi
fig.savefig("my_figure_300dpi.png", dpi = 300)
