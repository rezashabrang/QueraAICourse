import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model


def generate_data(n):
    rng = np.random.RandomState(1)
    x = np.sort(2 * np.pi * rng.rand(n))
    y = np.sin(x)
    return x, y


def polynomial_regression(n, path=None):
    c = 100
    x, y = generate_data(c)

    # TODO

    regr = linear_model.LinearRegression()

    # TODO

    # Plot outputs
    plt.scatter(x, y, color='black')

    # TODO

    plt.plot(x, np.sin(x), color='red', linewidth=2)

    plt.xticks(())
    plt.yticks(())

    if path:
        plt.savefig(path)

    return regr.coef_


def find_minimal_param():
    # TODO
    pass
