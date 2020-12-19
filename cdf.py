import numpy as np


def cdf(sample):
    with open('dists.npz', 'rb') as file:
        npzfile = np.load(file)
        normal_dist = npzfile['normal_dist']
        binomial_dist = npzfile['binomial_dist']
        poisson_dist = npzfile['posson_dist']
    x = sample.sort()
    y = np.arange(1, len(x) + 1) / len(x)

    return x,y

def draw_cdf(x, y):
    pass