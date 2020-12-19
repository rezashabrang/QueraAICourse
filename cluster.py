import pandas as pd

train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')


def get_features():
    kmeans_features = []  # TODO
    kmodes_features = []  # TODO
    return kmeans_features, kmodes_features


def transform_quality(quality):
    """
    :param quality: in [1,10]
    :return: transformed quality in [1,3]
    """
    quality = pd.DataFrame(quality)


