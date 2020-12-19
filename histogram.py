import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def show_hist(column, path=None):
    """
    Shows the histogram and number of elements in each bin
    :param column: name of column
    :param path: path of save figure
    :return: ndarray of number of elements in each bin
    """
    df_train = pd.read_csv('data/train.csv')
    q75, q25 = np.percentile(df_train[column], [75, 25])
    iqr = q75 - q25
    bin_count = (2 * iqr) / (np.power(np.size(df_train[column]), 1 / 3))
    bin_count = int(np.ceil(bin_count))
    b = np.size(df_train[column])
    # TODO
    hist = plt.hist(df_train[column], bins=bin_count, color="blue")

    if path:
        plt.savefig(path)

    return hist


show_hist('TotalBsmtSF', path=None)
plt.show()
