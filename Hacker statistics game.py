# NumPy is imported, seed is set
# Ensure the NumPy package is downloaded ('pip3 install numpy' in terminal, then 'python3')
from pkg_resources import ensure_directory
import numpy as np
import matplotlib AS plt

all_walks = []
for i in range(250) :
    random_walk = [0]

    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2 :
            step = max(0, step - 1)
        elif dice <= 5 :
            step = step + 1
        else :
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

np_aw = np.array(all_walks)
np_aw_t = np.transpose(np_aw)
ends = np_aw_t[-1, :]

plt.hist(ends)
plt.show()