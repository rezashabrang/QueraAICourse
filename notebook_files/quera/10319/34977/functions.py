import numpy as np
from numpy import unravel_index

def max_corr(dataframe):
    cr = dataframe.corr()
    triCor = cr.where(np.tril(np.ones(cr.shape),k=-1).astype(np.bool))
    triCor = triCor.abs().unstack().sort_values(ascending=False)
    return set(triCor.index[0])