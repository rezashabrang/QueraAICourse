import math
import numpy as np


# visits array is already loaded
def calc(last_days, k):
    landa = np.average(last_days)
    landa = float(landa)
    factorial = 1
    if int(k) >= 1:
        for j in range(1, int(k) + 1):
            factorial = factorial * j
    prob = math.exp(-landa) * pow(landa, int(k)) / factorial
    return prob
a = [1,2,3,4]
print(calc(a,3))