
import numpy as np
np.random.seed(123)
final_tails = []
for x in range(100):
    tails = [0]
    for y in range(10):
        coin = np.random.randint(0,2)
        tails.append(tails[y] + coin)

    final_tails.append(tails[-1])
print(final_tails)
