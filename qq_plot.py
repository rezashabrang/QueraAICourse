import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import preprocessing



def show_plot(column, path=None):
    df_train = pd.read_csv('data/train.csv')

    dft = df_train[column]
    dft = (dft-np.mean(dft))/np.std(dft)

    plt.clf()

    normal = np.random.normal(0, 1, 20000)
    percs = np.linspace(0, 100, 70)
    qn_normal = np.percentile(normal, percs)

    data = np.array(dft)
    qn_data = np.percentile(dft, percs)

    # TODO

    x = np.linspace(np.min((qn_normal.min(), qn_data.min())), np.max((qn_normal.max(), qn_data.max())))
    plt.plot(x, x, color="k", ls="--")
    plt.scatter(qn_normal,qn_data, color='blue')

    if path:
        plt.savefig(path)


show_plot('SalePrice', path=None)
plt.show()
