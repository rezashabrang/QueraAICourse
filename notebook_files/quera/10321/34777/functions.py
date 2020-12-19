#  IN THE NAME OF ALLAH

import numpy as np

class Linear_Regression:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.alpha0 = 0
        self.alpha1 = 0
        self.coefficients = [self.alpha0, self.alpha1]
    
    def fit(self, x, y):
        self.x = np.array(x)
        self.y = np.array(y)
        
        self.alpha1 =np.sum((self.x-np.average(self.x))*(self.y-np.average(self.y)))/np.sum((self.x-np.average(self.x))**2)
        self.alpha0 = np.average(self.y)-(self.alpha1)*np.average(self.x)
        
        self.coefficients = [self.alpha0, self.alpha1]
        return self
    
    def predict(self, x):
        #TODO
        return self.alpha0 + self.alpha1*x
    
    def mean_squared_error(self, y_test, y_pred):
        #TODO
        return (1/len(y_test))*np.sum((y_test-y_pred)**2)