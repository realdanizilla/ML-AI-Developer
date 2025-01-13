import numpy as np

class MyLinearRegression():
    def __init__(self):
        self.intercept = None
        self.coefficients = None

    def fit(self, X,y):
        Xb = np.c_[np.ones((X.shape[0],1)),X]
        beta = np.linalg.inv(Xb.T.dot(Xb)).dot(Xb.T).dot(y) # para poucos dados essa linha funciona, porém para muitos dados não
        self.intercept = beta[0]
        self.coefficients = beta[1:]

    def predict(self,X):
        Xb = np.c_[np.ones((X.shape[0],1)),X]
        return Xb.dot(np.r_[self.intercept,self.coefficients])