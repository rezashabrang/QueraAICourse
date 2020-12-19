#  IN THE NAME OF ALLAH
# modules
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
def regressor(latitude, longitude, train):
    train['index'] = np.round(np.array(train['index']/10))
    train['index'] = train['index'].astype(int)
    X = train[['Latitude','Longitude']]
    y = train['index']
    model = RandomForestClassifier(n_estimators = 200)
    model.fit(X,y)
    return 10*model.predict([[latitude, longitude]])
