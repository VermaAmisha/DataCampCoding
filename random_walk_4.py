import numpy as np

np.random.seed(123)
tails = [0]
for i in range(10):
    coin = np.random.randint(0,2)
    tails.append(tails[i] + coin)
print(tails)
